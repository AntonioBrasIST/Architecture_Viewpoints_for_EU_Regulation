using ExcelCreator.Doc.DocRepr;
using ExcelCreator.Doc.Structure;
using HtmlAgilityPack;
using System.Text.RegularExpressions;

namespace ExcelCreator
{
    /// <summary>
    /// Builds amendment articles from their table nesting rather than from the flattened
    /// paragraph stream used by the general-purpose parser.
    /// </summary>
    internal static class AmendmentArticleFactory
    {
        private static readonly HashSet<string> AmendmentArticles = ["59", "60", "61", "62", "63"];
        private static readonly Regex AmendmentMarkerRegex = new(@"^\(([0-9A-Za-z]+)\)$", RegexOptions.Compiled);

        internal static bool TryBuild(HtmlDocument document, string articleNumber, string articleTitle, out Orderable article)
        {
            article = null;
            if (AmendmentArticles.Contains(articleNumber))
            {
                var articleNode = document.GetElementbyId($"art_{articleNumber}");
                if (articleNode is null)
                {
                    return false;
                }

                var preamble = articleNode.ChildNodes.FirstOrDefault(node =>
                    node.Name.Equals("p", StringComparison.OrdinalIgnoreCase)
                    && node.GetAttributeValue("class", string.Empty).Contains("oj-normal", StringComparison.OrdinalIgnoreCase));
                if (preamble is null)
                {
                    return false;
                }

                article = new Orderable(articleNumber, articleTitle.CleanHtmlHyperLinks(), STRUCTURE.ARTICLE);
                var paragraph = new Orderable("1", ReadText(preamble), STRUCTURE.PARAGRAPH);
                article.GloballyOrderedItems.Add(paragraph);

                foreach (var table in articleNode.ChildNodes.Where(node => node.Name.Equals("table", StringComparison.OrdinalIgnoreCase)))
                {
                    var marker = ReadTableMarker(table);
                    if (TryReadDoraMarker(marker, out _))
                    {
                        paragraph.GloballyOrderedItems.Add(BuildLabeledTable(table, 1));
                    }
                    else
                    {
                        AddArticleContinuation(paragraph, table);
                    }
                }

                return true;
            }

            return false;
        }

        internal static bool TryBuildEidas2Document(HtmlDocument htmlDocument, out Document document)
        {
            document = null;
            if (!IsEidas2(htmlDocument))
            {
                return false;
            }

            var enactingTerms = htmlDocument.GetElementbyId("enc_1");
            var articleOneNode = enactingTerms?.ChildNodes.FirstOrDefault(node => node.Id == "art_1");
            var articleTwoNode = enactingTerms?.ChildNodes.FirstOrDefault(node => node.Id == "art_2");
            if (articleOneNode is null || articleTwoNode is null)
            {
                return false;
            }

            var articleOneTitle = ReadArticleTitle(articleOneNode);
            var articleTwoTitle = ReadArticleTitle(articleTwoNode);
            if (!TryBuildEidas2AmendmentArticle(articleOneNode, articleOneTitle, out var articleOne))
            {
                return false;
            }

            var articleTwo = BuildEidas2FinalArticle(articleTwoNode, articleTwoTitle);
            document = new Document();
            document.OrderedUpperStructure.Add(articleOne);
            document.OrderedUpperStructure.Add(articleTwo);
            return true;
        }

        private static bool TryBuildEidas2AmendmentArticle(HtmlNode articleNode, string articleTitle, out Orderable article)
        {
            article = null;
            var preamble = articleNode.ChildNodes.FirstOrDefault(node =>
                node.Name.Equals("p", StringComparison.OrdinalIgnoreCase)
                && node.GetAttributeValue("class", string.Empty).Contains("oj-normal", StringComparison.OrdinalIgnoreCase));
            if (preamble is null)
            {
                return false;
            }

            article = new Orderable("1", articleTitle.CleanHtmlHyperLinks(), STRUCTURE.ARTICLE);
            var paragraph = new Orderable("1", ReadText(preamble), STRUCTURE.PARAGRAPH);
            article.GloballyOrderedItems.Add(paragraph);

            foreach (var table in articleNode.ChildNodes.Where(node => node.Name.Equals("table", StringComparison.OrdinalIgnoreCase)))
            {
                if (!TryReadEidas2PointMarker(ReadTableMarker(table), out var pointNumber))
                {
                    return false;
                }

                paragraph.GloballyOrderedItems.Add(BuildEidas2Point(table, pointNumber));
            }

            return true;
        }

        private static Orderable BuildEidas2FinalArticle(HtmlNode articleNode, string articleTitle)
        {
            var contentParagraphs = articleNode.ChildNodes
                .Where(node => node.Name.Equals("p", StringComparison.OrdinalIgnoreCase)
                    && node.GetAttributeValue("class", string.Empty).Contains("oj-normal", StringComparison.OrdinalIgnoreCase))
                .ToList();
            if (contentParagraphs.Count == 0)
            {
                throw new InvalidOperationException("EIDAS2 Article 2 must contain enacting text.");
            }

            var article = new Orderable("2", articleTitle.CleanHtmlHyperLinks(), STRUCTURE.ARTICLE);
            var paragraph = new Orderable("1", ReadText(contentParagraphs[0]), STRUCTURE.PARAGRAPH);
            article.GloballyOrderedItems.Add(paragraph);

            var subParagraphCounter = 1;
            foreach (var contentParagraph in contentParagraphs.Skip(1))
            {
                paragraph.GloballyOrderedItems.Add(new Orderable(
                    subParagraphCounter.ToString(),
                    ReadText(contentParagraph),
                    STRUCTURE.SUBPARAGRAPH));
                subParagraphCounter++;
            }

            return article;
        }

        private static string ReadArticleTitle(HtmlNode articleNode)
        {
            var title = articleNode.SelectSingleNode("./div[contains(@class, 'eli-title')]/p");
            return title is null
                ? throw new InvalidOperationException("An EIDAS2 article must have a title.")
                : ReadText(title);
        }

        private static Orderable BuildEidas2Point(HtmlNode table, string pointNumber)
        {
            var row = FindFirstRow(table);
            var cells = row.ChildNodes.Where(node => node.Name.Equals("td", StringComparison.OrdinalIgnoreCase)).ToList();
            if (cells.Count < 2)
            {
                throw new InvalidOperationException("An EIDAS2 amendment table must contain a content cell.");
            }

            var contentCell = cells[1];
            var heading = contentCell.ChildNodes.FirstOrDefault(node =>
                node.Name.Equals("p", StringComparison.OrdinalIgnoreCase));
            if (heading is null)
            {
                throw new InvalidOperationException("An EIDAS2 amendment point must have text in its content cell.");
            }

            var point = new Orderable(pointNumber, ReadText(heading), STRUCTURE.POINT);
            foreach (var text in ReadEidas2ContinuationText(contentCell, heading))
            {
                point.GloballyOrderedItems.Add(new Orderable(string.Empty, text, STRUCTURE.AMENDMENTCONTINUATION));
            }

            return point;
        }

        private static IEnumerable<string> ReadEidas2ContinuationText(HtmlNode contentNode, HtmlNode heading)
        {
            foreach (var child in contentNode.ChildNodes)
            {
                if (child.NodeType != HtmlNodeType.Element)
                {
                    continue;
                }

                if (child.Name.Equals("p", StringComparison.OrdinalIgnoreCase))
                {
                    if (child != heading)
                    {
                        yield return ReadText(child);
                    }

                    continue;
                }

                if (child.Name.Equals("table", StringComparison.OrdinalIgnoreCase))
                {
                    var row = FindFirstRow(child);
                    foreach (var cell in row.ChildNodes
                        .Where(node => node.Name.Equals("td", StringComparison.OrdinalIgnoreCase))
                        .Skip(1))
                    {
                        foreach (var text in ReadEidas2ContinuationText(cell, heading))
                        {
                            yield return text;
                        }
                    }

                    continue;
                }

                foreach (var text in ReadEidas2ContinuationText(child, heading))
                {
                    yield return text;
                }
            }
        }

        private static bool IsEidas2(HtmlDocument document)
        {
            var canonicalLink = document.DocumentNode.SelectSingleNode("//link[@rel='canonical']");
            return canonicalLink?.GetAttributeValue("href", string.Empty)
                .Contains("/eli/reg/2024/1183/", StringComparison.OrdinalIgnoreCase) == true;
        }

        private static bool TryReadEidas2PointMarker(string text, out string marker)
        {
            var match = Regex.Match(text, @"^\((\d+)\)$", RegexOptions.CultureInvariant);
            marker = match.Success ? match.Groups[1].Value : string.Empty;
            return match.Success;
        }

        private static Orderable BuildLabeledTable(HtmlNode table, int depth)
        {
            var row = FindFirstRow(table);
            var cells = row.ChildNodes.Where(node => node.Name.Equals("td", StringComparison.OrdinalIgnoreCase)).ToList();
            var marker = ReadCellText(cells[0]);
            if (!TryReadDoraMarker(marker, out var value))
            {
                throw new InvalidOperationException("A DORA amendment table must begin with a labelled marker.");
            }

            var structure = depth switch
            {
                1 => STRUCTURE.POINT,
                2 => STRUCTURE.SUBPOINT,
                3 => STRUCTURE.INDENT,
                _ => throw new InvalidOperationException("DORA amendment nesting exceeds the available ID levels.")
            };

            var content = ReadContent(cells[1]).ToList();
            var heading = content.OfType<ParagraphContent>().FirstOrDefault();
            if (heading is null)
            {
                throw new InvalidOperationException("A DORA amendment marker must have text in its content cell.");
            }

            var orderable = new Orderable(value, heading.Text, structure);
            var firstParagraphSeen = false;
            var pointSubParagraphCounter = 1;
            var containsQuotedChildTable = content
                .OfType<TableContent>()
                .Any(tableContent => ReadTableMarker(tableContent.Table).StartsWith("‘", StringComparison.Ordinal));

            foreach (var item in content)
            {
                switch (item)
                {
                    case ParagraphContent paragraphContent:
                        if (!firstParagraphSeen)
                        {
                            firstParagraphSeen = true;
                        }
                        else
                        {
                            AddContinuation(orderable, depth, paragraphContent.Text, ref pointSubParagraphCounter);
                        }
                        break;
                    case TableContent tableContent:
                        var childMarker = ReadTableMarker(tableContent.Table);
                        if (!containsQuotedChildTable && depth < 3 && TryReadDoraMarker(childMarker, out _))
                        {
                            orderable.GloballyOrderedItems.Add(BuildLabeledTable(tableContent.Table, depth + 1));
                        }
                        else
                        {
                            foreach (var text in ReadQuotedTableText(tableContent.Table))
                            {
                                AddContinuation(orderable, depth, text, ref pointSubParagraphCounter);
                            }
                        }
                        break;
                }
            }

            return orderable;
        }

        private static void AddArticleContinuation(Orderable paragraph, HtmlNode table)
        {
            var counter = paragraph.GloballyOrderedItems.Count(item => item.Structure == STRUCTURE.SUBPARAGRAPH) + 1;
            foreach (var text in ReadQuotedTableText(table))
            {
                paragraph.GloballyOrderedItems.Add(new Orderable(counter.ToString(), text, STRUCTURE.SUBPARAGRAPH));
                counter++;
            }
        }

        private static void AddContinuation(Orderable parent, int parentDepth, string text, ref int pointSubParagraphCounter)
        {
            if (parentDepth == 1)
            {
                parent.GloballyOrderedItems.Add(new Orderable(
                    pointSubParagraphCounter.ToString(),
                    text,
                    STRUCTURE.POINTSUBPARAGRAPH));
                pointSubParagraphCounter++;
                return;
            }

            parent.GloballyOrderedItems.Add(new Orderable(string.Empty, text, STRUCTURE.AMENDMENTCONTINUATION));
        }

        private static IEnumerable<ContentItem> ReadContent(HtmlNode node)
        {
            foreach (var child in node.ChildNodes)
            {
                if (child.NodeType != HtmlNodeType.Element)
                {
                    continue;
                }

                if (child.Name.Equals("p", StringComparison.OrdinalIgnoreCase))
                {
                    yield return new ParagraphContent(ReadText(child));
                }
                else if (child.Name.Equals("table", StringComparison.OrdinalIgnoreCase))
                {
                    yield return new TableContent(child);
                }
                else
                {
                    foreach (var nested in ReadContent(child))
                    {
                        yield return nested;
                    }
                }
            }
        }

        private static IEnumerable<string> ReadQuotedTableText(HtmlNode table)
        {
            var row = FindFirstRow(table);
            var cells = row.ChildNodes.Where(node => node.Name.Equals("td", StringComparison.OrdinalIgnoreCase)).ToList();
            for (var index = 0; index < cells.Count; index++)
            {
                if (index == 0)
                {
                    continue;
                }

                foreach (var content in ReadContent(cells[index]))
                {
                    if (content is ParagraphContent paragraph)
                    {
                        yield return paragraph.Text;
                    }
                }
            }
        }

        private static HtmlNode FindFirstRow(HtmlNode table)
        {
            var row = table.SelectSingleNode("./tbody/tr")
                ?? table.SelectSingleNode("./tr");
            return row ?? throw new InvalidOperationException("A DORA amendment table must contain a row.");
        }

        private static string ReadTableMarker(HtmlNode table)
        {
            var row = FindFirstRow(table);
            var firstCell = row.ChildNodes.FirstOrDefault(node => node.Name.Equals("td", StringComparison.OrdinalIgnoreCase));
            return firstCell is null ? string.Empty : ReadCellText(firstCell);
        }

        private static bool TryReadDoraMarker(string text, out string marker)
        {
            var match = AmendmentMarkerRegex.Match(text);
            marker = match.Success ? match.Groups[1].Value : string.Empty;
            return match.Success;
        }

        private static string ReadText(HtmlNode node)
        {
            return node.InnerHtml.CleanHtmlHyperLinks();
        }

        private static string ReadCellText(HtmlNode cell)
        {
            var paragraph = cell.Descendants("p").FirstOrDefault();
            return paragraph is null ? string.Empty : ReadText(paragraph);
        }

        private abstract record ContentItem;
        private sealed record ParagraphContent(string Text) : ContentItem;
        private sealed record TableContent(HtmlNode Table) : ContentItem;
    }
}

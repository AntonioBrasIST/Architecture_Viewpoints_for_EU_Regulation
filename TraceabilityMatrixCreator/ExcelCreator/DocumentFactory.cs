using ExcelCreator.Doc.DocRepr;
using ExcelCreator.Doc.Structure;
using HtmlAgilityPack;
using System.Text;
using System.Text.Json;
using System.Text.RegularExpressions;

namespace ExcelCreator
{
    internal class DocumentFactory
    {
        private Regex _HTMLRegex;
        private Regex _HTMLTags;
        private Regex _recitalRegex;
        private List<Match> _htmlMatches;
        private string _outputDir;
        private HtmlDocument _htmlDocument;

        public DocumentFactory(string outputDir)
        {
            // =========================== REGEX ===========================
            _HTMLRegex = new Regex(
                @"(?<=<(p|span)[^>]*>)(?!(?<=<span[^>]*>).*?<span[^>]*>).*?(?=<\/\1>)",
                RegexOptions.Compiled | RegexOptions.Singleline | RegexOptions.IgnoreCase);
            _HTMLTags = new Regex(@"<[^>]*>", RegexOptions.Compiled);
            _recitalRegex = new Regex(@"^\((\d+)\)", RegexOptions.Compiled);
            _outputDir = outputDir;
        }

        internal void ProcessHTML(string HTML)
        {
            _htmlDocument = new HtmlDocument();
            _htmlDocument.LoadHtml(HTML);

            var startIndex = HTML.IndexOf(EUDocSeparators.RecitalBegin, StringComparison.OrdinalIgnoreCase);
            var endIndex = HTML.IndexOf(EUDocSeparators.DocumentEnd, StringComparison.OrdinalIgnoreCase);

            if (startIndex != -1)
            {
                var relevantText = HTML.Substring(
                    startIndex + EUDocSeparators.RecitalBegin.Length,
                    endIndex - (startIndex + EUDocSeparators.RecitalBegin.Length)
                ).Trim();
                var matches = _HTMLRegex.Matches(relevantText);
                _htmlMatches = matches.ToList();
            }
        }

        internal SortedList<int, string> ExtractRecitalsFromHTML()
        {
            if (_htmlMatches.Count > 0)
            {
                var recitals = new SortedList<int, string>();

                int i = 0;
                while (!_htmlMatches[i].Value.Contains(EUDocSeparators.RecitalEnd))
                {
                    var recitalText = new StringBuilder();
                    var recitalMatch = _recitalRegex.Match(_htmlMatches[i].Value);
                    // Index
                    var recitalIndex = int.Parse(recitalMatch.Groups[1].Value);
                    // Text
                    i++; // The next line has the text
                    recitalText.AppendLine(_HTMLTags.Replace(_htmlMatches[i].Value, ""));
                    // Check for paragraphs
                    int j = i + 1;
                    while (
                        !_htmlMatches[j].Value.Contains(EUDocSeparators.RecitalEnd)
                        && !_recitalRegex.Match(_htmlMatches[j].Value).Success
                    )
                    {
                        j++;
                        i++;
                        recitalText.AppendLine(_HTMLTags.Replace(_htmlMatches[j].Value, ""));
                    }

                    i++; // Move pointer to next Recital
                    recitals.Add(recitalIndex, recitalText.ToString());
                }

                var enactmentMarkerIndex = _htmlMatches.FindIndex(
                    match => match.Value.Contains(EUDocSeparators.RecitalEnd, StringComparison.Ordinal));
                if (enactmentMarkerIndex < 0)
                {
                    throw new InvalidOperationException("Could not find the enacting-terms marker after recital extraction.");
                }

                var firstEnactingTermIndex = _htmlMatches.FindIndex(
                    enactmentMarkerIndex + 1,
                    match => IsUpperHierarchyMarker(match.Value));
                if (firstEnactingTermIndex < 0)
                {
                    throw new InvalidOperationException("Could not find an upper hierarchy marker after the enacting-terms marker.");
                }

                _htmlMatches.RemoveRange(0, firstEnactingTermIndex);
                _htmlMatches.RemoveAll(match => IsFinalBindingFormula(match.Value));
                return recitals;
            }
            else 
            { 
                return null; 
            }
        }

        private static bool IsUpperHierarchyMarker(string value)
        {
            return EUDocSeparators.PartRegex.IsMatch(value)
                || EUDocSeparators.TitleRegex.IsMatch(value)
                || EUDocSeparators.ChapterRegex.IsMatch(value)
                || EUDocSeparators.SectionRegex.IsMatch(value)
                || EUDocSeparators.ArticleRegex.IsMatch(value);
        }

        private static bool IsFinalBindingFormula(string value)
        {
            var visibleText = Regex.Replace(value, @"<[^>]*>", string.Empty)
                .Replace('\u00a0', ' ');
            visibleText = Regex.Replace(visibleText, @"\s+", " ").Trim();

            return visibleText.Equals(
                "This Regulation shall be binding in its entirety and directly applicable in all Member States.",
                StringComparison.Ordinal);
        }

        internal Document ExtractEnactingTermsFromHTML()
        {
            if (_htmlMatches.Count > 0)
            {
                if (AmendmentArticleFactory.TryBuildEidas2Document(_htmlDocument, out var eidas2Document))
                {
                    SaveDocToJson(eidas2Document);
                    return eidas2Document;
                }

                Document doc = new Document();

                // Find Upper Hierarchy
                string value = _htmlMatches[0].Value;
                switch (value)
                {
                    case var _ when EUDocSeparators.PartRegex.IsMatch(value):
                        BuildFromPart(doc, _htmlMatches);
                        break;
                    case var _ when EUDocSeparators.TitleRegex.IsMatch(value):
                        BuildFromTitle(doc, _htmlMatches);
                        break;
                    case var _ when EUDocSeparators.ChapterRegex.IsMatch(value):
                        BuildFromChapter(doc, _htmlMatches);
                        break;
                    case var _ when EUDocSeparators.SectionRegex.IsMatch(value):
                        BuildFromSection(doc, _htmlMatches);
                        break;
                    case var _ when EUDocSeparators.ArticleRegex.IsMatch(value):
                        BuildFromArticle(doc, _htmlMatches);
                        break;
                    default:
                        throw new Exception("Unknown separator");
                }
                SaveDocToJson(doc);
                return doc;
            }
            else
            {
                return null;
            }
        }

        private void BuildFromPart(Document doc, List<Match> matchList)
        {
            throw new NotImplementedException();
        }

        private Orderable BuildPart(List<Match> matchList)
        {
            throw new NotImplementedException();
        }

        private void BuildFromTitle(Document doc, List<Match> matchList)
        {
            int lastMatch = 0;
            for (int i = 1; i < matchList.Count; i++)
            {
                if (EUDocSeparators.TitleRegex.IsMatch(matchList[i].Value))
                {
                    doc.OrderedUpperStructure.Add(BuildTitle(matchList.GetRange(lastMatch, i - lastMatch)));
                    lastMatch = i;
                }
            }

            doc.OrderedUpperStructure.Add(BuildTitle(matchList.GetRange(lastMatch, matchList.Count - lastMatch)));
        }

        private Orderable BuildTitle(List<Match> matchList)
        {
            var titleNumber = EUDocSeparators.TitleRegex.Match(matchList[0].Value).Groups[1].Value;
            var titleText = EUDocSeparators.TitleFinderRegex.Match(matchList[1].Value).Groups[1].Value;
            Console.WriteLine("Title " + titleNumber);

            var title = new Orderable(titleNumber, titleText.CleanHtmlHyperLinks(), STRUCTURE.TITLE);

            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 2;

            for (int i = 2; i < matchList.Count; i++)
            {
                bool isChapter = EUDocSeparators.ChapterRegex.IsMatch(matchList[i].Value);
                bool isArticle = EUDocSeparators.ArticleRegex.IsMatch(matchList[i].Value);

                if (isChapter || (isArticle && lastMatchStructure != STRUCTURE.CHAPTER))
                {
                    if (lastMatchStructure != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);
                        if (lastMatchStructure == STRUCTURE.CHAPTER)
                        {
                            title.GloballyOrderedItems.Add(BuildChapter(range));
                        }
                        else
                        {
                            title.GloballyOrderedItems.Add(BuildArticle(range));
                        }
                    }

                    lastMatchStructure = isChapter ? STRUCTURE.CHAPTER : STRUCTURE.ARTICLE;
                    lastMatch = i;
                }
            }

            var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);
            if (lastMatchStructure == STRUCTURE.CHAPTER)
            {
                title.GloballyOrderedItems.Add(BuildChapter(finalRange));
            }
            else if (lastMatchStructure == STRUCTURE.ARTICLE)
            {
                title.GloballyOrderedItems.Add(BuildArticle(finalRange));
            }

            return title;
        }

        private void BuildFromChapter(Document doc, List<Match> matchList)
        {
            // i = 0 is the chapter that matched here
            int lastMatch = 0;
            for (int i = 1; i < matchList.Count; i++)
            {
                if (EUDocSeparators.ChapterRegex.IsMatch(matchList[i].Value))
                {
                    var chapter = BuildChapter(matchList.GetRange(lastMatch, i - lastMatch));
                    doc.OrderedUpperStructure.Add(chapter);
                    lastMatch = i;
                }
            }
            doc.OrderedUpperStructure.Add(BuildChapter(matchList.GetRange(lastMatch, matchList.Count - lastMatch)));
        }

        private Orderable BuildChapter(List<Match> matchList)
        {
            var chapterNumber = EUDocSeparators.ChapterRegex.Match(matchList[0].Value).Groups[1].Value;
            var chapterTitle = EUDocSeparators.TitleFinderRegex.Match(matchList[1].Value).Groups[1].Value;
            Console.WriteLine("Chapter " + chapterNumber);

            var chapter = new Orderable(chapterNumber, chapterTitle.CleanHtmlHyperLinks(), STRUCTURE.CHAPTER);

            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 2;

            for (int i = 2; i < matchList.Count; i++)
            {
                bool isSection = EUDocSeparators.SectionRegex.IsMatch(matchList[i].Value);
                bool isArticle = EUDocSeparators.ArticleRegex.IsMatch(matchList[i].Value);

                if (isSection || (isArticle && lastMatchStructure != STRUCTURE.SECTION))
                {
                    // 1. If we have a pending match, "Close" it
                    if (lastMatchStructure != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);

                        if (lastMatchStructure == STRUCTURE.SECTION)
                            chapter.GloballyOrderedItems.Add(BuildSection(range));
                        else
                            chapter.GloballyOrderedItems.Add(BuildArticle(range));
                    }

                    // 2. "Start" the new match
                    lastMatchStructure = isSection ? STRUCTURE.SECTION : STRUCTURE.ARTICLE;
                    lastMatch = i;
                }
            }
            // Grab everything from the last found header to the end of the list
            var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);

            if (lastMatchStructure == STRUCTURE.SECTION)
                chapter.GloballyOrderedItems.Add(BuildSection(finalRange));
            else
                chapter.GloballyOrderedItems.Add(BuildArticle(finalRange));

            return chapter;
        }

        private void BuildFromSection(Document doc, List<Match> matchList)
        {

        }

        private Orderable BuildSection(List<Match> matchList)
        {
            var sectionNumber = EUDocSeparators.SectionRegex.Match(matchList[0].Value).Groups[1].Value;
            var sectionTitle = "";
            int lastMatch = 1;
            if (EUDocSeparators.TitleFinderRegex.IsMatch(matchList[1].Value))  // Section with Title
            {
                lastMatch++;
                sectionTitle = EUDocSeparators.TitleFinderRegex.Match(matchList[1].Value).Groups[1].Value;
            }
            Console.WriteLine("Section " + sectionNumber);
            var section = new Orderable(sectionNumber, sectionTitle.CleanHtmlHyperLinks(), STRUCTURE.SECTION);

            STRUCTURE lastMatchHierarchy = STRUCTURE.NONE;

            for (int i = lastMatch; i < matchList.Count; i++)
            {
                bool IsArticle = EUDocSeparators.ArticleRegex.IsMatch(matchList[i].Value);

                if (IsArticle)
                {
                    // 1. If we have a pending match, "Close" it
                    if (lastMatchHierarchy != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);
                        section.GloballyOrderedItems.Add(BuildArticle(range));
                    }

                    // 2. "Start" the new match
                    lastMatchHierarchy = STRUCTURE.ARTICLE;
                    lastMatch = i;
                }
            }
            // Grab everything from the last found header to the end of the list
            var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);
            section.GloballyOrderedItems.Add(BuildArticle(finalRange));

            return section;
        }

        private void BuildFromArticle(Document doc, List<Match> matchList)
        {
            int lastMatch = 0;
            for (int i = 1; i < matchList.Count; i++)
            {
                if (EUDocSeparators.ArticleRegex.IsMatch(matchList[i].Value))
                {
                    doc.OrderedUpperStructure.Add(BuildArticle(matchList.GetRange(lastMatch, i - lastMatch)));
                    lastMatch = i;
                }
            }

            doc.OrderedUpperStructure.Add(BuildArticle(matchList.GetRange(lastMatch, matchList.Count - lastMatch)));
        }

        private Orderable BuildArticle(List<Match> matchList)
        {
            var articleNumber = EUDocSeparators.ArticleRegex.Match(matchList[0].Value).Groups[1].Value;
            var articleTitle = matchList[1].Value.Trim();
            Console.WriteLine("Article " + articleNumber);

            if (AmendmentArticleFactory.TryBuild(_htmlDocument, articleNumber, articleTitle, out var amendmentArticle))
            {
                return amendmentArticle;
            }

            var article = new Orderable(articleNumber, articleTitle.CleanHtmlHyperLinks(), STRUCTURE.ARTICLE);

            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 2;
            if (!EUDocSeparators.ParagraphRegex.IsMatch(matchList[2].Value)) // If paragraph regex doesn't match, it's a single paragraph Article
            {
                  article.GloballyOrderedItems.Add(BuildParagraph(matchList.GetRange(2, matchList.Count - 2)));
            }
            else
            {
                for (int i = 2; i < matchList.Count; i++)
                {
                    bool isParagraph = EUDocSeparators.ParagraphRegex.IsMatch(matchList[i].Value);
                    bool isSubParagraph = EUDocSeparators.JustPlainTextRegex.IsMatch(matchList[i].Value);
                    if (isParagraph || (isSubParagraph && lastMatchStructure != STRUCTURE.PARAGRAPH))
                    {
                        // 1. If we have a pending match, "Close" it
                        if (lastMatchStructure != STRUCTURE.NONE)
                        {
                            var range = matchList.GetRange(lastMatch, i - lastMatch);

                            if (lastMatchStructure == STRUCTURE.PARAGRAPH) // -> No if
                                article.GloballyOrderedItems.Add(BuildParagraph(range));
                            //else
                            //article.SubParagraphs.Add(BuildSubParagraph(range)); // -> Remove this
                        }

                        // 2. "Start" the new match
                        lastMatchStructure = isParagraph ? STRUCTURE.PARAGRAPH : STRUCTURE.SUBPARAGRAPH;
                        lastMatch = i;
                    }
                }

                // Grab everything from the last found header to the end of the list
                var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);
                if (finalRange.Count > 0)
                {
                    article.GloballyOrderedItems.Add(BuildParagraph(finalRange));
                }
            }
            return article;
        }

        private Orderable BuildParagraph(List<Match> matchList)
        {
            // paragraphs begin with <number><dot><space><TEXT>
            var paragraphMatch = EUDocSeparators.ParagraphRegex.Match(matchList[0].Value);
            var paragraphNumber = paragraphMatch.Success ? paragraphMatch.Groups[1].Value : "1";
            var paragraphText = paragraphMatch.Success ? paragraphMatch.Groups[2].Value.Trim() : matchList[0].Value;
            Console.WriteLine("Paragraph " + paragraphNumber);
            var paragraph = new Orderable(paragraphNumber, paragraphText.CleanHtmlHyperLinks(), STRUCTURE.PARAGRAPH);
            var subparagraphCounter = 1;

            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 1;
            for (int i = 1; i < matchList.Count; i++)
            {
                bool isSubParagraph = EUDocSeparators.JustPlainTextRegex.IsMatch(matchList[i].Value) // TODO -> Validate this
                    && !EUDocSeparators.PointRegex.IsMatch(matchList[i - 1].Value)
                    && !EUDocSeparators.SubPointRegex.IsMatch(matchList[i - 1].Value)
                    && !EUDocSeparators.IndentChar.Equals(matchList[i - 1].Value);
                bool isPoint = EUDocSeparators.PointRegex.IsMatch(matchList[i].Value);
                bool isSubPoint = EUDocSeparators.SubPointRegex.IsMatch(matchList[i].Value)
                    && (EUDocSeparators.SubPointRegex.IsMatch(matchList[Math.Min(i + 2, matchList.Count - 1)].Value) || (EUDocSeparators.SubPointRegex.IsMatch(matchList[Math.Max(i - 2, 0)].Value)));

                if (isSubParagraph && IsPointContinuationAfterSubPoint(matchList, lastMatch, i, lastMatchStructure))
                {
                    isSubParagraph = false;
                }
                // TODO -> When does a sub-paragraph stop and another begin?
                // TODO -> Add sub-Point Detection but only when not included within Points
                if (isSubParagraph && lastMatchStructure != STRUCTURE.NONE && lastMatchStructure != STRUCTURE.SUBPARAGRAPH)
                {
                    // check if there are other Points in the rest of the text. If so, this subParagraph belongs to a point.
                    for(int j = i; j < matchList.Count; j++)
                    {
                        bool point = EUDocSeparators.PointRegex.IsMatch(matchList[j].Value);
                        if (point)
                        {
                            isSubParagraph = false;
                            break;
                        }
                    }
                }
                if ((isSubParagraph || (isPoint && lastMatchStructure != STRUCTURE.SUBPARAGRAPH)) && !isSubPoint)
                {
                    // 1. If we have a pending match, "Close" it
                    if (lastMatchStructure != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);

                        if (lastMatchStructure == STRUCTURE.SUBPARAGRAPH)
                        {
                            paragraph.GloballyOrderedItems.Add(BuildSubParagraph(range, subparagraphCounter));
                            subparagraphCounter++;
                        }
                        else
                            paragraph.GloballyOrderedItems.Add(BuildPoint(range));
                    }

                    // 2. "Start" the new match
                    lastMatchStructure = isSubParagraph ? STRUCTURE.SUBPARAGRAPH : STRUCTURE.POINT;
                    lastMatch = i;
                }
            }

            // Grab everything from the last found header to the end of the list
            var finalRange = matchList.GetRange(lastMatch, Math.Max(matchList.Count - lastMatch, 0));
            if (finalRange.Count != 0)
            {
                if (EUDocSeparators.JustPlainTextRegex.IsMatch(matchList[lastMatch].Value)
                    && !EUDocSeparators.PointRegex.IsMatch(matchList[lastMatch - 1].Value)
                    && !EUDocSeparators.SubPointRegex.IsMatch(matchList[lastMatch - 1].Value))
                {
                    paragraph.GloballyOrderedItems.Add(BuildSubParagraph(finalRange, subparagraphCounter));
                }
                else // Point
                {
                    paragraph.GloballyOrderedItems.Add(BuildPoint(finalRange));
                }
            }

            return paragraph;
        }

        private Orderable BuildSubParagraph(List<Match> matchList, int subparagraphCounter)
        {
            var subparagraph = new Orderable(subparagraphCounter.ToString(), matchList[0].Value.Trim().CleanHtmlHyperLinks(), STRUCTURE.SUBPARAGRAPH);
            Console.WriteLine("SubParagraph " + subparagraphCounter);

            // After this, everything is mandatorily a subPoint
            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 1;
            Orderable parentPoint = null;
            for (int i = 1; i < matchList.Count; i++)
            {
                var isSubPoint = IsNestedRomanSubPoint(matchList, i, lastMatchStructure);
                var isPoint = EUDocSeparators.PointRegex.IsMatch(matchList[i].Value) && !isSubPoint;

                if (isPoint || isSubPoint)
                {
                    // 1. If we have a pending match, "Close" it
                    if (lastMatchStructure != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);
                        if (lastMatchStructure == STRUCTURE.POINT)
                        {
                            parentPoint = BuildPoint(range);
                            subparagraph.GloballyOrderedItems.Add(parentPoint);
                        }
                        else
                        {
                            parentPoint.GloballyOrderedItems.Add(BuildSubPoint(range));
                        }
                    }

                    // 2. "Start" the new match
                    lastMatchStructure = isPoint ? STRUCTURE.POINT : STRUCTURE.SUBPOINT;
                    lastMatch = i;
                }
            }

            // Grab everything from the last found header to the end of the list
            if (matchList.Count > 1)
            {
                var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);
                if (lastMatchStructure == STRUCTURE.POINT)
                {
                    subparagraph.GloballyOrderedItems.Add(BuildPoint(finalRange));
                }
                else
                {
                    parentPoint.GloballyOrderedItems.Add(BuildSubPoint(finalRange));
                }
            }
            return subparagraph;
        }

        private Orderable BuildPoint(List<Match> matchList)
        {
            var pointLetter = EUDocSeparators.PointRegex.Match(matchList[0].Value).Groups[1].Value;
            var pointText = matchList[1].Value.Trim();
            Console.WriteLine("Point " + pointLetter);

            var point = new Orderable(pointLetter, pointText.CleanHtmlHyperLinks(), STRUCTURE.POINT);

            // After this, everything is mandatorily a subPoint
            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 2;
            int pointSubParagraphCounter = 1;
            for (int i = 2; i < matchList.Count; i++)
            {
                var isPointSubParagraph = EUDocSeparators.JustPlainTextRegex.IsMatch(matchList[i].Value)
                    && EUDocSeparators.JustPlainTextRegex.IsMatch(matchList[Math.Max(2, i - 1)].Value);
                var isSubPoint = EUDocSeparators.SubPointRegex.IsMatch(matchList[i].Value);
                if (isSubPoint || isPointSubParagraph)
                {
                    // 1. If we have a pending match, "Close" it
                    if (lastMatchStructure != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);
                        if (lastMatchStructure == STRUCTURE.SUBPOINT)
                            point.GloballyOrderedItems.Add(BuildSubPoint(range));
                        else
                            point.GloballyOrderedItems.Add(BuildPointSubParagraph(range, pointSubParagraphCounter++));
                    }

                    // 2. "Start" the new match
                    lastMatchStructure = isSubPoint ? STRUCTURE.SUBPOINT : STRUCTURE.POINTSUBPARAGRAPH;
                    lastMatch = i;
                }
            }

            // Grab everything from the last found header to the end of the list
            var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);
            if (finalRange.Count > 0)
            {
                if (lastMatchStructure == STRUCTURE.SUBPOINT)
                {
                    point.GloballyOrderedItems.Add(BuildSubPoint(finalRange));
                }
                else
                {
                    for (int i = 0; i < finalRange.Count; i++)
                    {
                        point.GloballyOrderedItems.Add(BuildPointSubParagraph(finalRange.GetRange(i, 1), pointSubParagraphCounter));
                    }
                }
            }

            return point;
        }

        private Orderable BuildPointSubParagraph(List<Match> matchList, int number)
        {
            var text = matchList.Count == 1 ? matchList.First().Value : throw new Exception("PointSubParagraph has more than one line.");
            return new Orderable(number.ToString(), text.CleanHtmlHyperLinks(), STRUCTURE.POINTSUBPARAGRAPH);
        }

        private Orderable BuildSubPoint(List<Match> matchList)
        {
            if (matchList.Count == 0)
            {
                return null;
            }
            var subPointLetter = EUDocSeparators.SubPointRegex.Match(matchList[0].Value).Groups[1].Value;
            var subPointText = matchList[1].Value.Trim();
            Console.WriteLine("SubPoint " + subPointLetter);

            var subPoint = new Orderable(subPointLetter, subPointText.CleanHtmlHyperLinks(), STRUCTURE.SUBPOINT);
            var indentCounter = 1;

            STRUCTURE lastMatchStructure = STRUCTURE.NONE;
            int lastMatch = 2;
            for (int i = 2; i < matchList.Count; i++)
            {
                // 1. If we have a pending match, "Close" it
                if (matchList[i].Value.Contains(EUDocSeparators.IndentChar)) // Is Indent
                {
                    if (lastMatchStructure != STRUCTURE.NONE)
                    {
                        var range = matchList.GetRange(lastMatch, i - lastMatch);
                        subPoint.GloballyOrderedItems.Add(BuildIndent(range, indentCounter));
                        indentCounter++;
                    }
                }

                // 2. "Start" the new match
                lastMatchStructure = STRUCTURE.INDENT;
                lastMatch = i;
            }

            // Grab everything from the last found header to the end of the list
            var finalRange = matchList.GetRange(lastMatch, matchList.Count - lastMatch);
            if (finalRange.Count > 0)
            {
                subPoint.GloballyOrderedItems.Add(BuildIndent(finalRange, indentCounter));
            }

            return subPoint;
        }

        private Orderable BuildIndent(List<Match> matchList, int indentCounter)
        {
            Console.WriteLine("Indent" + indentCounter.ToString());
            return new Orderable(indentCounter.ToString(), matchList[0].Value.Trim().CleanHtmlHyperLinks(), STRUCTURE.INDENT);
        }

        private static bool IsNestedRomanSubPoint(List<Match> matchList, int currentIndex, STRUCTURE previousStructure)
        {
            if (!EUDocSeparators.SubPointRegex.IsMatch(matchList[currentIndex].Value))
            {
                return false;
            }

            if (previousStructure == STRUCTURE.SUBPOINT)
            {
                return true;
            }

            if (previousStructure != STRUCTURE.POINT || currentIndex == 0)
            {
                return false;
            }

            var marker = EUDocSeparators.SubPointRegex.Match(matchList[currentIndex].Value).Groups[1].Value;
            var parentMarker = currentIndex >= 2
                ? EUDocSeparators.SubPointRegex.Match(matchList[currentIndex - 2].Value).Groups[1].Value
                : string.Empty;

            return marker.Equals("i", StringComparison.OrdinalIgnoreCase)
                && parentMarker.Equals("i", StringComparison.OrdinalIgnoreCase)
                && matchList[currentIndex - 1].Value.TrimEnd().EndsWith(':');
        }

        private static bool IsPointContinuationAfterSubPoint(
            List<Match> matchList,
            int pointStartIndex,
            int currentIndex,
            STRUCTURE lastMatchStructure)
        {
            if (lastMatchStructure != STRUCTURE.POINT || pointStartIndex >= currentIndex)
            {
                return false;
            }

            if (!Regex.IsMatch(
                    matchList[currentIndex].Value,
                    @"\bpoint\s+\([ivxlcdm]+\)\s+of\s+this\s+point\b",
                    RegexOptions.IgnoreCase))
            {
                return false;
            }

            for (int i = pointStartIndex; i < currentIndex; i++)
            {
                if (EUDocSeparators.SubPointRegex.IsMatch(matchList[i].Value))
                {
                    return true;
                }
            }

            return false;
        }


        // ============================= AUX =============================
        private void SaveDocToJson(Document doc)
        {
            // Configure the JSON for readability
            var options = new JsonSerializerOptions
            {
                WriteIndented = true
            };

            // Serialize the object to a string
            string jsonString = JsonSerializer.Serialize(doc, options);

            // Write the string to the file (creates or overwrites)
            File.WriteAllText(Path.Combine(_outputDir, "Doc.json"), jsonString);
        }
    }

    public static class StringCleanupExtensions
    {
        public static string CleanHtmlHyperLinks(this string text)
        {
            // Replace the match with an empty string
            var res = EUDocSeparators.CleanHtmlHyperLinks.Replace(text, "");

            // Clean up double spaces that might be left behind
            res = Regex.Replace(res, @"\s+", " ").Trim();

            return res;
        }
    }
}

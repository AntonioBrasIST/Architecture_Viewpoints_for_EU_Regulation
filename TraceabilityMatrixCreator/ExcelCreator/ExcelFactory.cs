using ExcelCreator.Doc.DocRepr;
using ExcelCreator.Doc.Structure;
using OfficeOpenXml;
using OfficeOpenXml.Style;
using System.Drawing;

namespace ExcelCreator
{
    public class ExcelFactory
    {
        // SYS
        private string _outputDir;
        private DocumentFactory _docFactory;
        Dictionary<Colour, Color> _colourDict;

        // Numbering
        private int _partCounter;
        private int _titleCounter;
        private int _chapterCounter;
        private int _sectionCounter;
        private int _articleCounter;
        private int _subArticleCounter;

        public ExcelFactory()
            : this(Path.Combine(GetRootDirectory(), "OutputDirectory"))
        {
        }

        internal ExcelFactory(string outputDir)
        {
            ExcelPackage.License.SetNonCommercialPersonal("ATB");
            ArgumentException.ThrowIfNullOrWhiteSpace(outputDir);
            _outputDir = outputDir;
            Directory.CreateDirectory(_outputDir);
            _docFactory = new DocumentFactory(_outputDir);
            BuildColourDict();
        }

        public void CreateExcelTraceabilityMatrixFromHTMLString(string HTML)
        {
            CreateExcelTraceabilityMatrixFromHTMLString(HTML, "FullFile");
        }

        public void CreateExcelTraceabilityMatrixFromHTMLString(string HTML, string outputFileName)
        {
            ArgumentException.ThrowIfNullOrWhiteSpace(outputFileName);
            _docFactory.ProcessHTML(HTML);
            var recitals = _docFactory.ExtractRecitalsFromHTML();
            var document = _docFactory.ExtractEnactingTermsFromHTML();
            var success = BuildMatrix(recitals, document, outputFileName);
        }

        private bool BuildMatrix(SortedList<int, string> recitals, Document doc, string outputFileName)
        {
            var excel = new ExcelPackage();
            var recitalSheet = excel.Workbook.Worksheets.Add("Recitals");
            var docSheet = excel.Workbook.Worksheets.Add("Enacting Terms");

            AddRecitalheaders(recitalSheet);
            BuildRecitals(recitalSheet, recitals);

            AddDocHeaders(docSheet);
            BuildEnactingTerms(docSheet, doc);

            MakeTable(docSheet);

            SaveExcelFile(excel, outputFileName);

            return false;
        }

        private void AddRecitalheaders(ExcelWorksheet recitalSheet)
        {
            recitalSheet.Cells["A1"].Value = "Number";
            recitalSheet.Cells["B1"].Value = "Text";
        }

        private void BuildRecitals(ExcelWorksheet recitalSheet, SortedList<int, string> recitals)
        {
            for (int i = 0; i < recitals.Count; i++)
            {
                recitalSheet.Cells[$"A{i+2}"].Value = i+1;
                recitalSheet.Cells[$"B{i+2}"].Value = recitals[i+1];
            }
        }

        private void AddDocHeaders(ExcelWorksheet docSheet)
        {
            docSheet.Cells["A1"].Value = "Part";
            docSheet.Cells["B1"].Value = "Title";
            docSheet.Cells["C1"].Value = "Chapter";
            docSheet.Cells["D1"].Value = "Section";
            docSheet.Cells["E1"].Value = "Article";
            docSheet.Cells["F1"].Value = "Paragraph";
            docSheet.Cells["G1"].Value = "Sub-Paragraph";
            docSheet.Cells["H1"].Value = "Point";
            docSheet.Cells["I1"].Value = "Point Sub-Paragraph";
            docSheet.Cells["J1"].Value = "Sub-Point";
            docSheet.Cells["K1"].Value = "Indent";
            docSheet.Cells["L1"].Value = "Text";
        }

        private void BuildEnactingTerms(ExcelWorksheet docSheet, Document doc)
        {
            StartContinousNumbering();
            var startingLayer = doc.UpperStructureLayer;
            switch (startingLayer) 
            {
                case STRUCTURE.PART:
                    BuildFromPart(docSheet, doc);
                    break;
                case STRUCTURE.TITLE:
                    BuildFromTitle(docSheet, doc);
                    break;
                case STRUCTURE.CHAPTER:
                    BuildFromChapter(docSheet, doc);
                    break;
                case STRUCTURE.SECTION:
                    BuildFromSection(docSheet, doc);
                    break;
                case STRUCTURE.ARTICLE:
                    BuildFromArticle(docSheet, doc);
                    break;
                default:
                    break;
            }

        }

        private void MakeTable(ExcelWorksheet docSheet)
        {
            var range = docSheet.Cells[$"A1:L{AllCountersAddedValue()+1}"];
            var table = docSheet.Tables.Add(range, "TraceabilityMatrix");
            table.TableStyle = OfficeOpenXml.Table.TableStyles.Light8; 
            AddGridLines(docSheet);
        }

        private void SaveExcelFile(ExcelPackage file, string filename)
        {
            file.SaveAs(new FileInfo(Path.Combine(_outputDir, filename + ".xlsx")));
        }

        private static string GetRootDirectory()
        {
            var currentDir = new DirectoryInfo(AppDomain.CurrentDomain.BaseDirectory);

            for (int i = 0; i < 5; i++)
            {
                // Check if any file in this directory ends with .sln
                if (currentDir.GetFiles("*.slnx").Any())
                {
                    return currentDir.FullName;
                }
                currentDir = currentDir.Parent;
            }

            // BOOM - Not found
            throw new Exception();
        }

        // ========================= COLOURING ========================
        #region Colour
        private void BuildColourDict()
        {
            _colourDict = new Dictionary<Colour, Color>
            {
                { Colour.POINT,         Color.FromArgb(220, 235, 252) }, // Soft Blue
                { Colour.INDENT,        Color.FromArgb(225, 245, 230) }, // Pale Green
                { Colour.PARAGRPH,      Color.FromArgb(255, 250, 205) }, // Lemon Chiffon
                { Colour.SUBPARAGRAPH,  Color.FromArgb(255, 235, 215) }, // Light Apricot
                { Colour.TITLE,         Color.FromArgb(240, 230, 255) }, // Pale Purple
                { Colour.PART,          Color.FromArgb(255, 230, 235) }, // Misty Rose
                { Colour.CHAPTER,       Color.FromArgb(220, 245, 255) }, // Very Light Cyan
                { Colour.ARTICLE,       Color.FromArgb(255, 210, 210) }, // Light Red/Coral
                { Colour.SUBPOINT,      Color.FromArgb(255, 240, 190) }, // Gold
                { Colour.SECTION,      Color.FromArgb(210, 245, 240) }   // Teal
            };
        }

        private Color GetColour(Colour colorName)
        {
            return _colourDict.TryGetValue(colorName, out var color) ? color : Color.White;
        }

        private void PaintRow(ExcelWorksheet docSheet, Colour colour)
        {
            var row = docSheet.Row(AllCountersAddedValue()+1);
            row.Style.Fill.PatternType = ExcelFillStyle.Solid;
            row.Style.Fill.BackgroundColor.SetColor(GetColour(colour));
        }

        private void AddGridLines(ExcelWorksheet docSheet)
        {
            var range = docSheet.Cells[1, 1, AllCountersAddedValue()+1, 11]; 
            range.Style.Border.Top.Style = ExcelBorderStyle.Thin;
            range.Style.Border.Bottom.Style = ExcelBorderStyle.Thin;
            range.Style.Border.Left.Style = ExcelBorderStyle.Thin;
            range.Style.Border.Right.Style = ExcelBorderStyle.Thin;
        }
        #endregion
        // ============================================================

        // ========================= BUILDING AS FIRST ========================
        #region UpperHierarchy Builders
        private void StartContinousNumbering()
        {
            _partCounter = 0;
            _titleCounter = 0;
            _chapterCounter = 0;
            _sectionCounter = 0;
            _articleCounter = 0;
            _subArticleCounter = 0;
        }

        private int AllCountersAddedValue()
        {
            return _partCounter + _titleCounter + _chapterCounter + _sectionCounter + _articleCounter + _subArticleCounter;
        }

        private void BuildFromPart(ExcelWorksheet docSheet, Document doc)
        {
            foreach (var part in doc.OrderedUpperStructure)
            {
                _partCounter++;
                PaintRow(docSheet, Colour.PART);
                docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = part.Number;
                docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = part.Text;
                foreach (var item in part.GloballyOrderedItems)
                {
                    if(item.Structure == STRUCTURE.ARTICLE)
                        BuildFromArticle(docSheet, item, part.Number, "", "", "");
                    else
                        BuildFromTitle(docSheet, item, part.Number);
                }
            }
        }

        private void BuildFromTitle(ExcelWorksheet docSheet, Document doc)
        {
            foreach (var title in doc.OrderedUpperStructure)
            {
                _titleCounter++;
                PaintRow(docSheet, Colour.TITLE);
                docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = "";
                docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = title.Number;
                docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = title.Text;
                foreach (var item in title.GloballyOrderedItems)
                {
                    if (item.Structure == STRUCTURE.ARTICLE)
                        BuildFromArticle(docSheet, item, "", title.Number, "", "");
                    else 
                        BuildFromChapter(docSheet, item , "", title.Number);
                }
            }
        }

        private void BuildFromChapter(ExcelWorksheet docSheet, Document doc)
        {
            foreach (var chapter in doc.OrderedUpperStructure)
            {
                _chapterCounter++;
                PaintRow(docSheet, Colour.CHAPTER);
                docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = "";
                docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = "";
                docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapter.Number;
                docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = chapter.Text;
                foreach (var item in chapter.GloballyOrderedItems)
                {
                    if (item.Structure == STRUCTURE.ARTICLE)
                        BuildFromArticle(docSheet, item, "", "", chapter.Number, "");
                    else
                        BuildFromSection(docSheet, item, "", "", chapter.Number);
                }
            }
        }

        private void BuildFromSection(ExcelWorksheet docSheet, Document doc)
        {
            foreach (var section in doc.OrderedUpperStructure)
            {
                _sectionCounter++;
                PaintRow(docSheet, Colour.SECTION);
                var sectionNameValue = !string.IsNullOrWhiteSpace(section.Text) ? section.Text : "";
                docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = "";
                docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = "";
                docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = "";
                docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = section.Number;
                docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = sectionNameValue;
                foreach (var item in section.GloballyOrderedItems)
                {
                    BuildFromArticle(docSheet, item, "", "", "", sectionNameValue);
                }
            }
        }

        private void BuildFromArticle(ExcelWorksheet docSheet, Document doc)
        {
            foreach (var article in doc.OrderedUpperStructure)
            {
                BuildFromArticle(docSheet, article, "", "", "", "");
            }
        }
        #endregion
        // ====================================================================

        // ========================= BUILDING AS BRANCH ========================
        #region Branching Builders
        private void BuildFromTitle(ExcelWorksheet docSheet, IOrderable title,
            string partNumber)
        {
            _titleCounter++;
            PaintRow(docSheet, Colour.TITLE);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = title.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = title.Text;
            foreach (var item in title.GloballyOrderedItems)
            {
                if (item.Structure == STRUCTURE.ARTICLE)
                    BuildFromArticle(docSheet, item, partNumber, title.Number, "", "");
                else
                    BuildFromChapter(docSheet, item, partNumber, title.Number);
            }
        }

        private void BuildFromChapter(ExcelWorksheet docSheet, IOrderable chapter,
            string partNumber, string titleNumber)
        {
            _chapterCounter++;
            PaintRow(docSheet, Colour.CHAPTER);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapter.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = chapter.Text;
            foreach (var item in chapter.GloballyOrderedItems)
            {
                if(item.Structure == STRUCTURE.ARTICLE)
                    BuildFromArticle(docSheet, item, partNumber, titleNumber, chapter.Number, "");
                else
                    BuildFromSection(docSheet, item, partNumber, titleNumber, chapter.Number);
            }

        }

        private void BuildFromSection(ExcelWorksheet docSheet, IOrderable section,
            string partNumber, string titleNumber, string chapterNumber)
        {
            _sectionCounter++;
            PaintRow(docSheet, Colour.SECTION);
            var sectionNameValue = !string.IsNullOrWhiteSpace(section.Text) ? section.Text : "";
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = section.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = sectionNameValue;
            foreach (var item in section.GloballyOrderedItems)
            {
                BuildFromArticle(docSheet, item, partNumber, titleNumber, chapterNumber, section.Number);
            }


        }

        private void BuildFromArticle(ExcelWorksheet docSheet, IOrderable article,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber)
        {
            _articleCounter++;
            PaintRow(docSheet, Colour.ARTICLE);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = article.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = article.Text;
            foreach (var item in article.GloballyOrderedItems)
            {
                BuildFromParagraph(docSheet, item, partNumber, titleNumber,
                    chapterNumber, sectionNumber, article.Number);
            }
        }

        private void BuildFromParagraph(ExcelWorksheet docSheet, IOrderable paragraph,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.PARAGRPH);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraph.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = paragraph.Text;
            foreach (var item in paragraph.GloballyOrderedItems)
            {
                if (item.Structure == STRUCTURE.SUBPARAGRAPH)
                    BuildFromSubParagraph(docSheet, item, partNumber, titleNumber,chapterNumber, sectionNumber, articleNumber, paragraph.Number);
                else
                    BuildFromPoint(docSheet, item, partNumber, titleNumber, chapterNumber, sectionNumber, articleNumber, paragraph.Number, "");
            }

        }

        private void BuildFromSubParagraph(ExcelWorksheet docSheet, IOrderable subParagraph,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber,
            string paragraphNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.SUBPARAGRAPH);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraphNumber;
            docSheet.Cells[$"G{AllCountersAddedValue() + 1}"].Value = subParagraph.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = subParagraph.Text;
            foreach (var item in subParagraph.GloballyOrderedItems)
            {
                if(item.Structure == STRUCTURE.POINT)
                    BuildFromPoint(docSheet, item, partNumber, titleNumber, chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraph.Number);
                else
                    BuildFromSubPoint(docSheet, item, partNumber, titleNumber, chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraph.Number, "");
            }

        }

        private void BuildFromPoint(ExcelWorksheet docSheet, IOrderable point,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber,
            string paragraphNumber, string subParagraphNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.POINT);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraphNumber;
            docSheet.Cells[$"G{AllCountersAddedValue() + 1}"].Value = subParagraphNumber;
            docSheet.Cells[$"H{AllCountersAddedValue() + 1}"].Value = point.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = point.Text;
            foreach (var item in point.GloballyOrderedItems)
            {
                if(item.Structure == STRUCTURE.SUBPOINT)
                    BuildFromSubPoint(docSheet, item, partNumber, titleNumber, chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraphNumber, point.Number);
                else if (item.Structure == STRUCTURE.AMENDMENTCONTINUATION)
                    BuildAmendmentContinuation(docSheet, item, partNumber, titleNumber, chapterNumber, sectionNumber,
                        articleNumber, paragraphNumber, subParagraphNumber, point.Number, "", "");
                else
                    BuildPointSubParagraph(docSheet, item, partNumber, titleNumber, chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraphNumber, point.Number);

            }
        }

        private void BuildPointSubParagraph(ExcelWorksheet docSheet, IOrderable subParagraph,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber,
            string paragraphNumber, string subParagraphNumber, string pointNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.POINT);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraphNumber;
            docSheet.Cells[$"G{AllCountersAddedValue() + 1}"].Value = subParagraphNumber;
            docSheet.Cells[$"H{AllCountersAddedValue() + 1}"].Value = pointNumber;
            docSheet.Cells[$"I{AllCountersAddedValue() + 1}"].Value = subParagraph.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = subParagraph.Text;
        }

        private void BuildFromSubPoint(ExcelWorksheet docSheet, IOrderable subPoint,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber,
            string paragraphNumber, string subParagraphNumber, string pointNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.SUBPOINT);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraphNumber;
            docSheet.Cells[$"G{AllCountersAddedValue() + 1}"].Value = subParagraphNumber;
            docSheet.Cells[$"H{AllCountersAddedValue() + 1}"].Value = pointNumber;
            docSheet.Cells[$"J{AllCountersAddedValue() + 1}"].Value = subPoint.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = subPoint.Text;
            foreach(var item in subPoint.GloballyOrderedItems)
            {
                if (item.Structure == STRUCTURE.AMENDMENTCONTINUATION)
                {
                    BuildAmendmentContinuation(docSheet, item, partNumber, titleNumber,
                        chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraphNumber, pointNumber, subPoint.Number, "");
                }
                else
                {
                    BuildFromIndent(docSheet, item, partNumber, titleNumber,
                        chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraphNumber, pointNumber, subPoint.Number);
                }
            }

        }

        private void BuildFromIndent(ExcelWorksheet docSheet, IOrderable indent,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber,
            string paragraphNumber, string subParagraphNumber, string pointNumber, string subPointNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.INDENT);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraphNumber;
            docSheet.Cells[$"G{AllCountersAddedValue() + 1}"].Value = subParagraphNumber;
            docSheet.Cells[$"H{AllCountersAddedValue() + 1}"].Value = pointNumber;
            docSheet.Cells[$"J{AllCountersAddedValue() + 1}"].Value = subPointNumber;
            docSheet.Cells[$"K{AllCountersAddedValue() + 1}"].Value = indent.Number;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = indent.Text;

            foreach (var item in indent.GloballyOrderedItems)
            {
                if (item.Structure == STRUCTURE.AMENDMENTCONTINUATION)
                {
                    BuildAmendmentContinuation(docSheet, item, partNumber, titleNumber,
                        chapterNumber, sectionNumber, articleNumber, paragraphNumber, subParagraphNumber, pointNumber, subPointNumber, indent.Number);
                }
            }
        }

        private void BuildAmendmentContinuation(ExcelWorksheet docSheet, IOrderable continuation,
            string partNumber, string titleNumber, string chapterNumber, string sectionNumber, string articleNumber,
            string paragraphNumber, string subParagraphNumber, string pointNumber, string subPointNumber, string indentNumber)
        {
            _subArticleCounter++;
            PaintRow(docSheet, Colour.SUBPOINT);
            docSheet.Cells[$"A{AllCountersAddedValue() + 1}"].Value = partNumber;
            docSheet.Cells[$"B{AllCountersAddedValue() + 1}"].Value = titleNumber;
            docSheet.Cells[$"C{AllCountersAddedValue() + 1}"].Value = chapterNumber;
            docSheet.Cells[$"D{AllCountersAddedValue() + 1}"].Value = sectionNumber;
            docSheet.Cells[$"E{AllCountersAddedValue() + 1}"].Value = articleNumber;
            docSheet.Cells[$"F{AllCountersAddedValue() + 1}"].Value = paragraphNumber;
            docSheet.Cells[$"G{AllCountersAddedValue() + 1}"].Value = subParagraphNumber;
            docSheet.Cells[$"H{AllCountersAddedValue() + 1}"].Value = pointNumber;
            docSheet.Cells[$"J{AllCountersAddedValue() + 1}"].Value = subPointNumber;
            docSheet.Cells[$"K{AllCountersAddedValue() + 1}"].Value = indentNumber;
            docSheet.Cells[$"L{AllCountersAddedValue() + 1}"].Value = continuation.Text;
        }
        #endregion
        // =====================================================================

        // ================================AUX==================================
        //private void BuildFromOrderableEnumerable(IEnumerable<IOrderable> orderables)
        //{
        //    foreach (var item in orderables)
        //    {
        //        switch (item.Structure)
        //        {
        //            case STRUCTURE.ARTICLE:
        //                BuildFromArticle(docSheet, (Article)item, part.Number, "", "", "");
        //            break;
        //        }
        //    }

        //    if (item.Structure == STRUCTURE.ARTICLE)
        //        BuildFromArticle(docSheet, (Article)item, part.Number, "", "", "");
        //    else
        //        BuildFromTitle(docSheet, (Title)item, part.Number);
        //}
        // =====================================================================

    }
}

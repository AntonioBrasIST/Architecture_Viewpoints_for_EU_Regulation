using ExcelCreator;
using OfficeOpenXml;
using Xunit;

namespace TraceabilityMatrixCreator.Tests;

public sealed class CsaTitleHierarchyRegressionTests
{
    private static readonly string[] EnactingHeaders =
    [
        "Part",
        "Title",
        "Chapter",
        "Section",
        "Article",
        "Paragraph",
        "Sub-Paragraph",
        "Point",
        "Point Sub-Paragraph",
        "Sub-Point",
        "Indent",
        "Text"
    ];

    [Fact]
    public void GeneratedCsaWorkbookBuildsTitlesAboveChaptersAndArticles()
    {
        var outputDirectory = Path.Combine(Path.GetTempPath(), $"traceability-matrix-{Guid.NewGuid():N}");
        Directory.CreateDirectory(outputDirectory);

        try
        {
            var sourcePath = Path.Combine(AppContext.BaseDirectory, "Fixtures", "CSA.html");
            var factory = new ExcelFactory(outputDirectory);
            factory.CreateExcelTraceabilityMatrixFromHTMLString(File.ReadAllText(sourcePath), "CSA");
            var workbookPath = Path.Combine(outputDirectory, "CSA.xlsx");

            Assert.True(File.Exists(workbookPath));

            using var package = new ExcelPackage(new FileInfo(workbookPath));
            Assert.Equal(["Recitals", "Enacting Terms"], package.Workbook.Worksheets.Select(sheet => sheet.Name).ToArray());

            var worksheet = package.Workbook.Worksheets["Enacting Terms"];
            Assert.NotNull(worksheet);
            Assert.Equal(EnactingHeaders, ReadCells(worksheet, 1, 1, 12));

            Assert.Equal(["I", "II", "III", "IV"], FindTitleRows(worksheet).Select(row => worksheet.Cells[row, 2].GetValue<string>()));

            var titleTwoRow = FindRow(worksheet, title: "II", chapter: "", article: "");
            var chapterOneRow = FindRow(worksheet, title: "II", chapter: "I", article: "");
            var articleThreeRow = FindRow(worksheet, title: "II", chapter: "I", article: "3");
            var articleFortySixRow = FindRow(worksheet, title: "III", chapter: "", article: "46");

            Assert.True(titleTwoRow < chapterOneRow);
            Assert.True(chapterOneRow < articleThreeRow);
            Assert.Equal("Mandate and objectives", worksheet.Cells[chapterOneRow, 12].GetValue<string>());
            Assert.Equal("European cybersecurity certification framework", worksheet.Cells[articleFortySixRow, 12].GetValue<string>());

            AssertSectionAndArticleRange(worksheet, "1", "Management Board", 14, 18);
            AssertSectionAndArticleRange(worksheet, "2", "Executive Board", 19, 19);
            AssertSectionAndArticleRange(worksheet, "3", "Executive Director", 20, 20);
            AssertSectionAndArticleRange(
                worksheet,
                "4",
                "ENISA Advisory Group, Stakeholder Cybersecurity Certification Group and National Liaison Officers Network",
                21,
                23);
            AssertSectionAndArticleRange(worksheet, "5", "Operation", 24, 28);

            var articleIds = Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
                .Select(row => worksheet.Cells[row, 5].GetValue<string>())
                .Where(articleId => !string.IsNullOrEmpty(articleId))
                .Distinct()
                .ToArray();

            Assert.Equal(Enumerable.Range(1, 69).Select(articleId => articleId.ToString()), articleIds);
        }
        finally
        {
            Directory.Delete(outputDirectory, recursive: true);
        }
    }

    private static IEnumerable<int> FindTitleRows(ExcelWorksheet worksheet)
    {
        return Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
            .Where(row => !string.IsNullOrEmpty(worksheet.Cells[row, 2].GetValue<string>()))
            .Where(row => string.IsNullOrEmpty(worksheet.Cells[row, 3].GetValue<string>()))
            .Where(row => string.IsNullOrEmpty(worksheet.Cells[row, 5].GetValue<string>()));
    }

    private static int FindRow(ExcelWorksheet worksheet, string title, string chapter, string article)
    {
        return Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
            .Single(row => worksheet.Cells[row, 2].GetValue<string>() == title
                && (worksheet.Cells[row, 3].GetValue<string>() ?? string.Empty) == chapter
                && (worksheet.Cells[row, 5].GetValue<string>() ?? string.Empty) == article
                && Enumerable.Range(6, 6).All(column => string.IsNullOrEmpty(worksheet.Cells[row, column].GetValue<string>())));
    }

    private static void AssertSectionAndArticleRange(
        ExcelWorksheet worksheet,
        string section,
        string expectedTitle,
        int firstArticle,
        int lastArticle)
    {
        var sectionRow = Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
            .Single(row => worksheet.Cells[row, 2].GetValue<string>() == "II"
                && worksheet.Cells[row, 3].GetValue<string>() == "III"
                && worksheet.Cells[row, 4].GetValue<string>() == section
                && string.IsNullOrEmpty(worksheet.Cells[row, 5].GetValue<string>())
                && Enumerable.Range(6, 6).All(column => string.IsNullOrEmpty(worksheet.Cells[row, column].GetValue<string>())));
        Assert.Equal(expectedTitle, worksheet.Cells[sectionRow, 12].GetValue<string>());

        foreach (var article in Enumerable.Range(firstArticle, lastArticle - firstArticle + 1))
        {
            var articleRow = FindRow(worksheet, "II", "III", article.ToString());
            Assert.Equal(section, worksheet.Cells[articleRow, 4].GetValue<string>());
        }
    }

    private static string[] ReadCells(ExcelWorksheet worksheet, int row, int firstColumn, int lastColumn)
    {
        return Enumerable.Range(firstColumn, lastColumn - firstColumn + 1)
            .Select(column => worksheet.Cells[row, column].GetValue<string>() ?? string.Empty)
            .ToArray();
    }
}

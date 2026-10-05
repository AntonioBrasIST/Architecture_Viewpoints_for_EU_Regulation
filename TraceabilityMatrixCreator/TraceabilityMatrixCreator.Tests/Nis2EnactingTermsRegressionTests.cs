using ExcelCreator;
using OfficeOpenXml;
using Xunit;

namespace TraceabilityMatrixCreator.Tests;

public sealed class Nis2EnactingTermsRegressionTests
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
    public void GeneratedNis2WorkbookStartsAtChapterOneAndRetainsArticleSequence()
    {
        var outputDirectory = Path.Combine(Path.GetTempPath(), $"traceability-matrix-{Guid.NewGuid():N}");
        Directory.CreateDirectory(outputDirectory);

        try
        {
            var sourcePath = Path.Combine(AppContext.BaseDirectory, "Fixtures", "NIS2.html");
            var factory = new ExcelFactory(outputDirectory);
            factory.CreateExcelTraceabilityMatrixFromHTMLString(File.ReadAllText(sourcePath), "NIS2");
            var workbookPath = Path.Combine(outputDirectory, "NIS2.xlsx");

            Assert.True(File.Exists(workbookPath));

            using var package = new ExcelPackage(new FileInfo(workbookPath));
            Assert.Equal(["Recitals", "Enacting Terms"], package.Workbook.Worksheets.Select(sheet => sheet.Name).ToArray());

            var worksheet = package.Workbook.Worksheets["Enacting Terms"];
            Assert.NotNull(worksheet);
            Assert.Equal(EnactingHeaders, ReadCells(worksheet, 1, 1, 12));
            Assert.Equal(
                ["", "", "I", "", "", "", "", "", "", "", "", "GENERAL PROVISIONS"],
                ReadCells(worksheet, 2, 1, 12));

            var articleIds = Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
                .Select(row => worksheet.Cells[row, 5].GetValue<string>())
                .Where(articleId => !string.IsNullOrEmpty(articleId))
                .Distinct()
                .ToArray();

            Assert.Equal(Enumerable.Range(1, 46).Select(articleId => articleId.ToString()), articleIds);
        }
        finally
        {
            Directory.Delete(outputDirectory, recursive: true);
        }
    }

    private static string[] ReadCells(ExcelWorksheet worksheet, int row, int firstColumn, int lastColumn)
    {
        return Enumerable.Range(firstColumn, lastColumn - firstColumn + 1)
            .Select(column => worksheet.Cells[row, column].GetValue<string>() ?? string.Empty)
            .ToArray();
    }
}

using ExcelCreator;
using OfficeOpenXml;
using Xunit;

namespace TraceabilityMatrixCreator.Tests;

public sealed class Eidas2RootArticleRegressionTests
{
    [Fact]
    public void GeneratedEidas2WorkbookSupportsDirectArticleRoot()
    {
        var outputDirectory = Path.Combine(Path.GetTempPath(), $"traceability-matrix-{Guid.NewGuid():N}");
        Directory.CreateDirectory(outputDirectory);

        try
        {
            var sourcePath = Path.Combine(AppContext.BaseDirectory, "Fixtures", "EIDAS2.html");
            var factory = new ExcelFactory(outputDirectory);
            factory.CreateExcelTraceabilityMatrixFromHTMLString(File.ReadAllText(sourcePath), "EIDAS2");
            var workbookPath = Path.Combine(outputDirectory, "EIDAS2.xlsx");

            Assert.True(File.Exists(workbookPath));

            using var package = new ExcelPackage(new FileInfo(workbookPath));
            Assert.Equal(["Recitals", "Enacting Terms"], package.Workbook.Worksheets.Select(sheet => sheet.Name).ToArray());

            var worksheet = package.Workbook.Worksheets["Enacting Terms"];
            Assert.NotNull(worksheet);
            Assert.Equal("Article", worksheet.Cells[1, 5].GetValue<string>());
            Assert.Equal("1", worksheet.Cells[2, 5].GetValue<string>());
            Assert.Equal("Amendments to Regulation (EU) No 910/2014", worksheet.Cells[2, 12].GetValue<string>());

            var pointIds = Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
                .Select(row => worksheet.Cells[row, 8].GetValue<string>())
                .Where(pointId => !string.IsNullOrEmpty(pointId))
                .Distinct()
                .ToArray();
            Assert.Equal(Enumerable.Range(1, 53).Select(number => number.ToString()), pointIds);

            Assert.Contains(
                Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
                    .Select(row => worksheet.Cells[row, 12].GetValue<string>()),
                text => text.Contains("Subject matter", StringComparison.Ordinal));

            var articleIds = Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
                .Select(row => worksheet.Cells[row, 5].GetValue<string>())
                .Where(articleId => !string.IsNullOrEmpty(articleId))
                .Distinct()
                .ToArray();

            Assert.Equal(["1", "2"], articleIds);
        }
        finally
        {
            Directory.Delete(outputDirectory, recursive: true);
        }
    }
}

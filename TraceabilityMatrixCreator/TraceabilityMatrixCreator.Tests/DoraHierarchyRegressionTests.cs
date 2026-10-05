using System.Security.Cryptography;
using System.Text;
using System.Text.Encodings.Web;
using System.Text.Json;
using ExcelCreator;
using OfficeOpenXml;
using Xunit;

namespace TraceabilityMatrixCreator.Tests;

public sealed class DoraHierarchyRegressionTests
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

    private static readonly JsonSerializerOptions CanonicalJsonOptions = new()
    {
        Encoder = JavaScriptEncoder.UnsafeRelaxedJsonEscaping
    };

    [Fact]
    public void GeneratedDoraWorkbookMatchesApprovedDoraHierarchy()
    {
        var outputDirectory = Path.Combine(Path.GetTempPath(), $"traceability-matrix-{Guid.NewGuid():N}");
        Directory.CreateDirectory(outputDirectory);

        try
        {
            var workbookPath = GenerateDoraWorkbook(outputDirectory);

            using var package = new ExcelPackage(new FileInfo(workbookPath));
            Assert.Equal(["Recitals", "Enacting Terms"], package.Workbook.Worksheets.Select(sheet => sheet.Name).ToArray());

            var worksheet = package.Workbook.Worksheets["Enacting Terms"];
            Assert.NotNull(worksheet);
            Assert.Equal(EnactingHeaders, ReadCells(worksheet, 1, 1, 12));

            Assert.Equal(
                ["", "", "II", "I", "5", "2", "1", "i", "", "i", ""],
                ReadCells(worksheet, 135, 1, 11));
            Assert.Equal(
                ["", "", "II", "I", "5", "2", "1", "i", "", "ii", ""],
                ReadCells(worksheet, 136, 1, 11));
            Assert.Equal(
                ["", "", "II", "I", "5", "2", "1", "i", "", "iii", ""],
                ReadCells(worksheet, 137, 1, 11));
            Assert.Equal(
                ["", "", "V", "II", "35", "1", "", "d", "1", "", ""],
                ReadCells(worksheet, 588, 1, 11));

            Assert.Equal(
                "arrangements concluded with ICT third-party service providers on the use of ICT services,",
                worksheet.Cells[135, 12].GetValue<string>());
            Assert.Equal(
                "For the purpose of point (iv) of this point, ICT third-party service providers shall, using the template referred to in Article 41(1), point (b), transmit the information regarding subcontracting to the Lead Overseer.",
                worksheet.Cells[588, 12].GetValue<string>());

            Assert.Equal(
                ["", "", "IX", "I", "58", "3", "", "", "", "", ""],
                ReadCells(worksheet, 834, 1, 11));
            Assert.Equal(909, worksheet.Dimension.End.Row);
            Assert.Equal(
                ["", "", "IX", "II", "64", "", "", "", "", "", ""],
                ReadCells(worksheet, 907, 1, 11));
            Assert.Equal(
                ["", "", "IX", "II", "64", "1", "1", "", "", "", ""],
                ReadCells(worksheet, 909, 1, 11));
            Assert.DoesNotContain(
                "This Regulation shall be binding in its entirety and directly applicable in all Member States.",
                Enumerable.Range(2, worksheet.Dimension.End.Row - 1)
                    .Select(row => worksheet.Cells[row, 12].GetValue<string>()));

            AssertAmendmentIds(worksheet);
            AssertManifest(worksheet);
        }
        finally
        {
            Directory.Delete(outputDirectory, recursive: true);
        }
    }

    private static string GenerateDoraWorkbook(string outputDirectory)
    {
        var sourcePath = Path.Combine(AppContext.BaseDirectory, "Fixtures", "DORA.html");
        var source = File.ReadAllText(sourcePath);
        var factory = new ExcelFactory(outputDirectory);
        factory.CreateExcelTraceabilityMatrixFromHTMLString(source, "DORA");
        var workbookPath = Path.Combine(outputDirectory, "DORA.xlsx");
        Assert.True(File.Exists(workbookPath));
        Assert.False(File.Exists(Path.Combine(outputDirectory, "FullFile.xlsx")));
        return workbookPath;
    }

    private static void AssertManifest(ExcelWorksheet worksheet)
    {
        var manifestPath = Path.Combine(AppContext.BaseDirectory, "Fixtures", "dora_in_scope_row_manifest.json");
        var manifest = JsonSerializer.Deserialize<DoraInScopeRowManifest>(
            File.ReadAllText(manifestPath),
            new JsonSerializerOptions { PropertyNameCaseInsensitive = true });

        Assert.NotNull(manifest);
        Assert.Equal("Enacting Terms", manifest.Sheet);
        Assert.Equal(2, manifest.FirstWorksheetRow);
        Assert.Equal(909, manifest.LastWorksheetRow);
        Assert.Equal(908, manifest.RowHashes.Count);

        foreach (var entry in manifest.RowHashes)
        {
            var worksheetRow = int.Parse(entry.Key);
            var rowHash = ComputeRowHash(ReadCells(worksheet, worksheetRow, 1, 12));
            Assert.Equal(entry.Value, rowHash);
        }
    }

    private static void AssertAmendmentIds(ExcelWorksheet worksheet)
    {
        var expectationPath = Path.Combine(AppContext.BaseDirectory, "Fixtures", "dora_amendment_id_expectations.json");
        var expectations = JsonSerializer.Deserialize<DoraAmendmentIdExpectations>(
            File.ReadAllText(expectationPath),
            new JsonSerializerOptions { PropertyNameCaseInsensitive = true });

        Assert.NotNull(expectations);
        Assert.Equal(835, expectations.FirstWorksheetRow);
        Assert.Equal(906, expectations.LastWorksheetRow);
        Assert.Equal(72, expectations.RowIds.Count);

        foreach (var expectation in expectations.RowIds)
        {
            var worksheetRow = int.Parse(expectation.Key);
            Assert.Equal(expectation.Value, ReadCells(worksheet, worksheetRow, 1, 11));
        }
    }

    private static string[] ReadCells(ExcelWorksheet worksheet, int row, int firstColumn, int lastColumn)
    {
        return Enumerable.Range(firstColumn, lastColumn - firstColumn + 1)
            .Select(column => worksheet.Cells[row, column].GetValue<string>() ?? string.Empty)
            .ToArray();
    }

    private static string ComputeRowHash(string[] values)
    {
        var serializedValues = JsonSerializer.Serialize(values, CanonicalJsonOptions);
        return Convert.ToHexString(SHA256.HashData(Encoding.UTF8.GetBytes(serializedValues))).ToLowerInvariant();
    }

    private sealed class DoraInScopeRowManifest
    {
        public string Sheet { get; init; } = string.Empty;
        public int FirstWorksheetRow { get; init; }
        public int LastWorksheetRow { get; init; }
        public Dictionary<string, string> RowHashes { get; init; } = [];
    }

    private sealed class DoraAmendmentIdExpectations
    {
        public int FirstWorksheetRow { get; init; }
        public int LastWorksheetRow { get; init; }
        public Dictionary<string, string[]> RowIds { get; init; } = [];
    }
}

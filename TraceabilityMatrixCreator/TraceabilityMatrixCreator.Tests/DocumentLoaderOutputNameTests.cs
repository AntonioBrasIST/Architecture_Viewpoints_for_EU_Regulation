using TraceabilityMatrixCreator.App;
using Xunit;

namespace TraceabilityMatrixCreator.Tests;

public sealed class DocumentLoaderOutputNameTests
{
    [Theory]
    [InlineData("DORA", LoadDocument.DORA)]
    [InlineData("EIDAS2", LoadDocument.EIDAS2)]
    [InlineData("NIS2", LoadDocument.NIS2)]
    [InlineData("CSA", LoadDocument.CSA)]
    [InlineData("32022R2554", LoadDocument.DORA)]
    [InlineData("32024R1183", LoadDocument.EIDAS2)]
    [InlineData("32022L2555", LoadDocument.NIS2)]
    [InlineData("32019R0881", LoadDocument.CSA)]
    public void SelectorResolvesLegislationNameOrCelex(string selector, LoadDocument expectedDocument)
    {
        Assert.True(DocumentLoader.TryResolveDocument(selector, out var document));
        Assert.Equal(expectedDocument, document);
    }

    [Fact]
    public void SelectorRejectsBlankAndUnknownValues()
    {
        Assert.False(DocumentLoader.TryResolveDocument(null!, out _));
        Assert.False(DocumentLoader.TryResolveDocument("   ", out _));
        Assert.False(DocumentLoader.TryResolveDocument("32022R0000", out _));
    }

    [Theory]
    [InlineData(LoadDocument.DORA, "DORA-CELEX:32022R2554")]
    [InlineData(LoadDocument.EIDAS2, "EIDAS2-CELEX:32024R1183")]
    [InlineData(LoadDocument.NIS2, "NIS2-CELEX:32022L2555")]
    [InlineData(LoadDocument.CSA, "CSA-CELEX:32019R0881")]
    public void OutputFileNameIncludesLegislationAndCelex(LoadDocument document, string expectedFileName)
    {
        var documentLoader = new DocumentLoader();

        Assert.Equal(expectedFileName, documentLoader.GetOutputFileName(document));
    }
}

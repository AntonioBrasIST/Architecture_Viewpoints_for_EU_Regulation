using ExcelCreator;
using Microsoft.Extensions.Configuration;

namespace TraceabilityMatrixCreator.App
{
    public class TraceabilityMatrixCreatorApp
    {
        private ExcelFactory _excelFactory;
        private DocumentLoader _docLoader;

        public TraceabilityMatrixCreatorApp()
        {
            // AppSettings
            IConfiguration config = new ConfigurationBuilder()
                .SetBasePath(Directory.GetCurrentDirectory())
                .AddJsonFile("Settings/AppSettings.json")
                .Build();

            // DocLoader
            _docLoader = new DocumentLoader();

            // Excel Factory
            _excelFactory = new ExcelFactory();
        }

        public async Task<int> RunAsync(string[] args)
        {
            if (args.Length != 1 || !DocumentLoader.TryResolveDocument(args[0], out var documentToLoad))
            {
                Console.Error.WriteLine("Usage: TraceabilityMatrixCreator <DORA|EIDAS2|NIS2|CSA|CELEX>");
                return 2;
            }

            var doc = await _docLoader.GetDocumentHTMLAsync(documentToLoad);
            _excelFactory.CreateExcelTraceabilityMatrixFromHTMLString(doc, _docLoader.GetOutputFileName(documentToLoad));
            return 0;
        }
    }
}

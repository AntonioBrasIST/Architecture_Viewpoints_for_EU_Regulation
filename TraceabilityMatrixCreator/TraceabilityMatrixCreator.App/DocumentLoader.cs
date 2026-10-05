namespace TraceabilityMatrixCreator.App
{
    public class DocumentLoader
    {
        private string _documentDir;

        public DocumentLoader()
        {
            _documentDir = Path.Combine(GetRootDirectory(), "Documents");
        }

        public async Task<string> GetDocumentHTMLAsync(LoadDocument documentToLoad)
        {
            var pathToDoc = GetDocumentPath(documentToLoad);
            return await File.ReadAllTextAsync(pathToDoc);
        }

        public string GetOutputFileName(LoadDocument documentToLoad)
        {
            var (_, celex) = GetDocumentDefinition(documentToLoad);
            return $"{documentToLoad}-CELEX:{celex}";
        }

        public static bool TryResolveDocument(string selector, out LoadDocument documentToLoad)
        {
            documentToLoad = default;
            if (string.IsNullOrWhiteSpace(selector))
            {
                return false;
            }

            var normalizedSelector = selector.Trim();
            foreach (var candidate in Enum.GetValues<LoadDocument>())
            {
                var (_, celex) = GetDocumentDefinition(candidate);
                if (candidate.ToString().Equals(normalizedSelector, StringComparison.OrdinalIgnoreCase)
                    || celex.Equals(normalizedSelector, StringComparison.OrdinalIgnoreCase))
                {
                    documentToLoad = candidate;
                    return true;
                }
            }

            return false;
        }

        private string GetRootDirectory()
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

        private string GetDocumentPath(LoadDocument documentToLoad)
        {
            var (fileName, _) = GetDocumentDefinition(documentToLoad);
            return Path.Combine(_documentDir, fileName);
        }

        private static (string FileName, string Celex) GetDocumentDefinition(LoadDocument documentToLoad)
        {
            return documentToLoad switch
            {
                LoadDocument.DORA => ("L_2022333EN.01000101.xml.html", "32022R2554"),
                LoadDocument.EIDAS2 => ("L_202401183EN.000101.fmx.xml.html", "32024R1183"),
                LoadDocument.NIS2 => ("L_2022333EN.01008001.xml.html", "32022L2555"),
                LoadDocument.CSA => ("L_2019151EN.01001501.xml.html", "32019R0881"),
                _ => throw new ArgumentOutOfRangeException(nameof(documentToLoad), documentToLoad, null),
            };
        }
    }

    public enum LoadDocument
    {
        DORA,
        EIDAS2,
        NIS2,
        CSA
    }
}

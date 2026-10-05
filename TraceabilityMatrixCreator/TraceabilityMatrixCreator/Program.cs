using TraceabilityMatrixCreator.App;

namespace TraceabilityMatrixCreator
{
    internal class Program
    {
        static async Task<int> Main(string[] args)
        {
            var app = new TraceabilityMatrixCreatorApp();
            return await app.RunAsync(args);
        }
    }
}

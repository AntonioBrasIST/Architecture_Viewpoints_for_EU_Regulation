using System.Text.Json.Serialization;

namespace ExcelCreator.Doc.Structure
{
    internal class Orderable : IOrderable
    {
        [JsonInclude]
        public List<IOrderable> GloballyOrderedItems { get; }
        [JsonInclude]
        public string Number { get; set; }
        [JsonInclude]
        public string Text { get; set; }

        public STRUCTURE Structure { get; }

        public Orderable(string number, string text, STRUCTURE myStructure)
        {
            Text = text;
            Number = number;
            GloballyOrderedItems = new List<IOrderable>();
            Structure = myStructure;
        }
    }
}

using ExcelCreator.Doc.Structure;

namespace ExcelCreator.Doc.DocRepr
{
    internal class Document
    {
        internal STRUCTURE? UpperStructureLayer { get
            {
                return OrderedUpperStructure.FirstOrDefault()?.Structure;
            }
        }

        internal List<IOrderable> OrderedUpperStructure { get; }

        public Document()
        {
            OrderedUpperStructure = new List<IOrderable>();
        }
    }
}

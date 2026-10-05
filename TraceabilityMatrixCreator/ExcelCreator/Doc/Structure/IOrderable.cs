namespace ExcelCreator.Doc.Structure
{
    internal interface IOrderable
    {
        public STRUCTURE Structure { get; }

        public List<IOrderable> GloballyOrderedItems { get; }
        
        public string Number { get; }
        public string Text { get; }
    }
}

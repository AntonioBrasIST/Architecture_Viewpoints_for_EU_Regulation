using System.Text.RegularExpressions;

namespace ExcelCreator
{
    internal static class EUDocSeparators
    {
        // Document level Regex's

        /// <summary>
        /// Never matches
        /// </summary>
        internal static readonly Regex PartRegex = new Regex(
            @"(?!)",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);
        /// <summary>
        /// Finds the current Title and its number in Roman numerals.
        /// </summary>
        internal static readonly Regex TitleRegex = new Regex(
            @"(?:>|^)Title\s+(X{0,2}(?:IX|IV|V?I{0,3}))(?:<|$)",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);
        /// <summary>
        /// Finds the current Chapter and it's number in roman numerals
        /// </summary>
        internal static readonly Regex ChapterRegex = new Regex(
            @"(?:>|^)Chapter\s+(X{0,2}(?:IX|IV|V?I{0,3}))(?:<|$)",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);
        /// <summary>
        /// Finds the current Section and its number in Arabic or Roman numerals.
        /// </summary>
        internal static readonly Regex SectionRegex = new Regex(
            @"(?:>|^)Section\s+(\d+|X{0,2}(?:IX|IV|V?I{0,3}))(?:<|$)",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);
        /// <summary>
        /// 
        /// </summary>
        internal static readonly Regex ArticleRegex = new Regex(
            @"^Article\s+(\d+)$",
            RegexOptions.Compiled | RegexOptions.IgnoreCase);
        /// <summary>
        /// 
        /// </summary>
        internal static readonly Regex TitleFinderRegex = new Regex(
            @"<span[^>]*>([^<>]+)</span>",
            RegexOptions.Compiled | RegexOptions.Singleline);

        // Article Level Regex's

        /// <summary>
        /// Checks if current string is a paragraph i.e. begins with a dotted number
        /// </summary>
        internal static readonly Regex ParagraphRegex = new Regex(
            @"^(\d+)\.(.*)$",
            RegexOptions.Compiled | RegexOptions.Singleline);
        /// <summary>
        /// Checks if current string is a sub paragraph i.e. does not start with any listing notation
        /// </summary>
        internal static readonly Regex JustPlainTextRegex = new Regex(
            @"^(?!(?:\d+\.|\([a-zA-Z0-9]+\)|\([ivxlcdmIVXLCDM]+\)|[—]))",
            RegexOptions.Compiled | RegexOptions.Singleline);
        /// <summary>
        /// 
        /// </summary>
        internal static readonly Regex PointRegex = new Regex(
            @"^\(([a-zA-Z0-9]+)\)$",
            RegexOptions.Compiled | RegexOptions.Singleline);
        /// <summary>
        /// 
        /// </summary>
        internal static readonly Regex SubPointRegex = new Regex(
            @"^\((?i)(X{0,3}(?:IX|IV|V?I{0,3}))\)$",
            RegexOptions.Compiled | RegexOptions.Singleline | RegexOptions.IgnoreCase);

        internal static readonly string IndentChar = "—";

        internal static readonly IEnumerable<string> ParenthesizedNumbers
            = Enumerable.Range(1, 200).Select(i => $"({i})").ToList();
        internal static readonly IEnumerable<string> DottedNumbers 
            = Enumerable.Range(1, 200).Select(i => $"{i}.").ToList();
        internal static readonly IEnumerable<string> ParenthesizedLetters 
            = Enumerable.Range(0, 26).Select(i => $"({(char)('a' + i)})").ToList();
        internal static readonly IEnumerable<string> ParenthesizedRoman
            = new[] { "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x" } 
            .Select(r => $"({r})").ToList();

        internal static readonly string RecitalBegin = "Whereas:";
        internal static readonly string RecitalEnd = "HAVE ADOPTED THIS";
        internal static readonly string DocumentEnd = "Done at ";

        internal static readonly Regex CleanHtmlHyperLinks = new Regex(
            @"<a\b[^>]*>.*?</a>",
            RegexOptions.Compiled | RegexOptions.Singleline);
    }
}

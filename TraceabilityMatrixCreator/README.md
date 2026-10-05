# TraceabilityMatrixCreator

Creates Excel legal traceability matrices from the bundled EUR-Lex source
documents. Each generated workbook contains `Recitals` and `Enacting Terms`
worksheets. The latter records the legal hierarchy from Part through Indent
alongside each source-text fragment.

## Run

Run one selected legislation from the repository root:

```bash
(cd TraceabilityMatrixCreator/TraceabilityMatrixCreator.App && dotnet run --project ../TraceabilityMatrixCreator -- DORA)
```

The selector is case-insensitive. It accepts either the legislation name or
its CELEX identifier:

| Legislation | Name selector | CELEX selector |
| --- | --- | --- |
| Digital Operational Resilience Act | `DORA` | `32022R2554` |
| eIDAS 2 | `EIDAS2` | `32024R1183` |
| NIS2 Directive | `NIS2` | `32022L2555` |
| Cybersecurity Act | `CSA` | `32019R0881` |

For example:

```bash
(cd TraceabilityMatrixCreator/TraceabilityMatrixCreator.App && dotnet run --project ../TraceabilityMatrixCreator -- 32022L2555)
```

The workbook is written to `TraceabilityMatrixCreator/OutputDirectory` as
`<Legislation>-CELEX:<CELEX>.xlsx`, for example
`DORA-CELEX:32022R2554.xlsx`. Invalid, blank, or missing selectors print a
usage message and return exit code `2`.

## Limitation

Amendment hierarchy handling is known to be incomplete. It is outside this
tool's current scope, so amendment rows should not be treated as an
authoritative reconstruction of the amended instrument.

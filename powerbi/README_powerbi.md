# Humanitarian Finance & Operations Dashboard - Power BI Pack

This folder contains the implementation pack for rebuilding a public LinkedIn-ready Power BI dashboard from synthetic, anonymised humanitarian finance and operations data.

No confidential data, real invoices, suppliers, bank details, beneficiary names, transaction IDs, or sensitive operational records are used.

## Files Included

Data:

- `data/synthetic/humanitarian_finance_fact.csv`
- `data/synthetic/dim_projects.csv`
- `data/synthetic/dim_donors.csv`
- `data/synthetic/dim_locations.csv`
- `data/synthetic/dim_budget_lines.csv`
- `data/synthetic/dim_beneficiaries.csv`
- `data/synthetic/generate_synthetic_powerbi_data.mjs`

Power BI instructions:

- `powerbi/dax/measures.md`
- `powerbi/model/modeling_instructions.md`
- `powerbi/layout/dashboard_wireframe.md`
- `powerbi/README_powerbi.md`

## Dashboard Goal

Build a portfolio dashboard titled:

**Humanitarian Finance & Operations Dashboard**

The dashboard is designed to demonstrate:

- Humanitarian finance analysis
- Donor and grant monitoring
- Budget vs actual tracking
- CVA operational analysis
- Beneficiary reach monitoring
- Compliance and audit readiness
- Geographic and branch-level management

## Build Sequence

### 1. Open Power BI Desktop

Create a new blank report.

### 2. Import CSV Files

Go to **Home > Get data > Text/CSV** and import each CSV from `data/synthetic`.

Import these files:

- `humanitarian_finance_fact.csv`
- `dim_projects.csv`
- `dim_donors.csv`
- `dim_locations.csv`
- `dim_budget_lines.csv`
- `dim_beneficiaries.csv`

Check data types:

- `Date`, `Start_Date`, `End_Date`: Date
- Budgets, expenditure, commitments, forecast, transfer value: Decimal number or Whole number
- Beneficiary and household fields: Whole number
- Latitude and longitude: Decimal number

### 3. Generate Or Expand The Fact Table To 500+ Rows

Preferred option:

If Node.js is available, run the generator from the repository root:

```powershell
node data/synthetic/generate_synthetic_powerbi_data.mjs
```

It writes `data/synthetic/humanitarian_finance_fact.csv` with 540 fully synthetic transaction rows.

Power BI-only option:

The source fact CSV includes the full transaction structure and synthetic seed records. To create a 500+ row synthetic working table directly in Power BI Desktop:

1. Open **Transform data**.
2. Select `humanitarian_finance_fact`.
3. Open **Advanced Editor**.
4. Replace the query with this Power Query pattern, adjusting the first line if Power BI generated a different source step name:

```powerquery
let
    Source = Csv.Document(File.Contents("C:\Users\edebu\Codex\humanitarian_portfolio\data\synthetic\humanitarian_finance_fact.csv"),[Delimiter=",", Columns=45, Encoding=65001, QuoteStyle=QuoteStyle.Csv]),
    PromotedHeaders = Table.PromoteHeaders(Source, [PromoteAllScalars=true]),
    ChangedTypes = Table.TransformColumnTypes(PromotedHeaders,{
        {"Date", type date}, {"Year", Int64.Type}, {"Approved_Budget", type number}, {"Revised_Budget", type number},
        {"Actual_Expenditure", type number}, {"Commitment", type number}, {"Forecast_Expenditure", type number},
        {"Beneficiaries_Planned", Int64.Type}, {"Beneficiaries_Reached", Int64.Type}, {"Women", Int64.Type},
        {"Men", Int64.Type}, {"Girls", Int64.Type}, {"Boys", Int64.Type}, {"Transfer_Value", type number},
        {"Households_Reached", Int64.Type}, {"Total_Cash_Transferred", type number}
    }),
    Copies = List.Transform({1..90}, each Table.AddColumn(ChangedTypes, "Synthetic_Copy", (row) => _, Int64.Type)),
    Combined = Table.Combine(Copies),
    AddedIndex = Table.AddIndexColumn(Combined, "Synthetic_Index", 1, 1, Int64.Type),
    RebuiltTransactionId = Table.AddColumn(AddedIndex, "Transaction_ID_New", each "TXN-SYN-" & Text.PadStart(Text.From([Synthetic_Index]), 4, "0"), type text),
    RemovedOldId = Table.RemoveColumns(RebuiltTransactionId, {"Transaction_ID"}),
    RenamedId = Table.RenameColumns(RemovedOldId, {{"Transaction_ID_New", "Transaction_ID"}}),
    AdjustedActuals = Table.TransformColumns(RenamedId, {
        {"Actual_Expenditure", each Number.Round(_ * (0.82 + Number.Mod(_, 11) / 100), 0), type number},
        {"Commitment", each Number.Round(_ * (0.75 + Number.Mod(_, 7) / 100), 0), type number},
        {"Forecast_Expenditure", each Number.Round(_ * (0.88 + Number.Mod(_, 9) / 100), 0), type number}
    }),
    RemovedHelper = Table.RemoveColumns(AdjustedActuals, {"Synthetic_Copy", "Synthetic_Index"})
in
    RemovedHelper
```

This produces 540 synthetic fact rows from the seed records while keeping transaction IDs unique.

### 4. Create The Model

Use the star schema described in `powerbi/model/modeling_instructions.md`.

Central fact table:

- `humanitarian_finance_fact`

Dimensions:

- `dim_projects`
- `dim_donors`
- `dim_locations`
- `dim_budget_lines`
- `dim_beneficiaries`
- `Calendar`

Create the `Calendar` table using the DAX script in `modeling_instructions.md`, then mark it as a date table.

### 5. Add DAX Measures

Open `powerbi/dax/measures.md` and copy the measures into Power BI.

Recommended approach:

1. Create a blank table called `Measures`.
2. Add all DAX measures into that table.
3. Format currency, percentage, and count fields.
4. Organise measures into display folders: Finance, Beneficiaries, CVA, Compliance, Scope.

### 6. Build Report Pages

Use `powerbi/layout/dashboard_wireframe.md` as the page-by-page build guide.

Create these report pages:

1. Executive Overview
2. Budget vs Actual
3. Donor & Grant Monitoring
4. CVA Operations
5. Beneficiary Reach
6. Compliance & Audit Readiness
7. Geographic / Branch View

### 7. Apply Visual Style

Use a professional humanitarian design:

- White or light grey canvas
- Dark readable typography
- Red Cross-inspired red accents
- Simple cards and charts
- No flashy gradients
- No fake startup-style visuals

Suggested colors:

- Red accent: `#D71920`
- Dark text: `#222222`
- Secondary text: `#5F6368`
- Light background: `#F7F7F7`
- Card background: `#FFFFFF`
- Warning amber: `#F5A623`
- Positive green: `#2E7D32`

### 8. Suggested Report-Level Slicers

Use compact slicers across the top or left side:

- Year
- Country
- Project
- Donor
- Sector
- Budget Category
- Audit Risk Level

### 9. LinkedIn Export Recommendations

For LinkedIn, export or screenshot:

- Page 1: Executive Overview
- Page 4: CVA Operations
- Page 6: Compliance & Audit Readiness

Use a 16:9 canvas. Keep KPI cards readable at feed size. Add a visible note in your portfolio page or post:

> Synthetic and anonymised dataset. No confidential or beneficiary-identifiable data used.

## Portfolio Positioning Text

You can use this short description in your portfolio:

> This Power BI dashboard uses a fully synthetic humanitarian finance and operations dataset to demonstrate budget monitoring, donor compliance, CVA operations, beneficiary reach analysis, and audit readiness across multi-country emergency response contexts.

## Manual Row Expansion Option

If you want a larger dataset inside Power BI Desktop, you can duplicate the fact table in Power Query by appending it to itself several times, then add an index column and replace `Transaction_ID` with:

```powerquery
"TXN-SYN-" & Text.PadStart(Text.From([Index]), 4, "0")
```

This keeps the dataset synthetic and allows stress-testing visuals with 500+ rows while preserving the structure of the source CSV.

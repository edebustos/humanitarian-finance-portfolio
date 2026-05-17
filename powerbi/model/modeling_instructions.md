# Power BI Modeling Instructions

## Import

Import the CSV files from `data/synthetic`:

- `humanitarian_finance_fact.csv`
- `dim_projects.csv`
- `dim_donors.csv`
- `dim_locations.csv`
- `dim_budget_lines.csv`
- `dim_beneficiaries.csv`

Use **Get data > Text/CSV** in Power BI Desktop. Confirm that numeric fields are imported as decimal or whole number and that `Date`, `Start_Date`, and `End_Date` are date fields.

## Star Schema

Use `humanitarian_finance_fact` as the central fact table. Keep all dimensions as lookup tables with one-to-many relationships flowing from dimension to fact.

Recommended relationships:

| From dimension | Column | To fact | Column | Cardinality | Cross-filter |
|---|---:|---|---:|---|---|
| `dim_projects` | `Project_ID` | `humanitarian_finance_fact` | `Project_ID` | One-to-many | Single |
| `dim_donors` | `Donor_ID` | `humanitarian_finance_fact` | `Donor_ID` | One-to-many | Single |
| `dim_locations` | `Location` | `humanitarian_finance_fact` | `Location` | One-to-many | Single |
| `dim_budget_lines` | `Budget_Line_ID` | `humanitarian_finance_fact` | `Budget_Line_ID` | One-to-many | Single |
| `dim_beneficiaries` | `Sector` | `humanitarian_finance_fact` | `Sector` | One-to-many | Single |
| `Calendar` | `Date` | `humanitarian_finance_fact` | `Date` | One-to-many | Single |

If Power BI warns that `dim_beneficiaries[Sector]` is not unique, create a small sector dimension instead or relate `dim_beneficiaries` only when using beneficiary group analysis. For the portfolio dashboard, sector filters can also come directly from the fact table.

## Calendar Table

Create a calendar table in Power BI using:

```DAX
Calendar =
ADDCOLUMNS (
    CALENDAR (
        MIN ( humanitarian_finance_fact[Date] ),
        MAX ( humanitarian_finance_fact[Date] )
    ),
    "Year", YEAR ( [Date] ),
    "Quarter", "Q" & FORMAT ( [Date], "Q" ),
    "Month Number", MONTH ( [Date] ),
    "Month", FORMAT ( [Date], "MMMM" ),
    "Year-Month", FORMAT ( [Date], "YYYY-MM" )
)
```

Then select the table and choose **Mark as date table**, using `Calendar[Date]`.

## Data Categories

Set:

- `dim_locations[Latitude]` as Latitude.
- `dim_locations[Longitude]` as Longitude.
- `Country` as Country/Region.
- `Location` as Place.

## Model Hygiene

- Hide technical IDs only after relationships and measures are working.
- Hide raw numeric columns used only by measures, such as `Actual_Expenditure`, `Commitment`, and `Revised_Budget`.
- Keep slicer fields visible: `Country`, `Project_Name`, `Donor_Name`, `Sector`, `Budget_Category`, `Audit_Risk_Level`, `Documentation_Status`, and `Reporting_Status`.
- Use measure folders: Finance, Beneficiaries, CVA, Compliance, Scope.

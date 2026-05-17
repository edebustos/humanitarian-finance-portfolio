# DAX Measures

Create these measures in Power BI Desktop after importing the CSV files. Suggested table: create a blank table named `Measures` and store all measures there.

## Core Finance

```DAX
Total Budget =
SUM ( humanitarian_finance_fact[Approved_Budget] )

Revised Budget =
SUM ( humanitarian_finance_fact[Revised_Budget] )

Total Expenditure =
SUM ( humanitarian_finance_fact[Actual_Expenditure] )

Total Commitments =
SUM ( humanitarian_finance_fact[Commitment] )

Forecast Expenditure =
SUM ( humanitarian_finance_fact[Forecast_Expenditure] )

Remaining Budget =
[Revised Budget] - [Total Expenditure] - [Total Commitments]

Burn Rate % =
DIVIDE ( [Total Expenditure], [Revised Budget] )

Forecast Variance =
[Revised Budget] - [Forecast Expenditure]

Budget Variance =
[Revised Budget] - [Total Expenditure]

Utilisation % =
DIVIDE ( [Total Expenditure] + [Total Commitments], [Revised Budget] )
```

## Beneficiary Reach

```DAX
Beneficiaries Reached =
SUM ( humanitarian_finance_fact[Beneficiaries_Reached] )

Beneficiaries Planned =
SUM ( humanitarian_finance_fact[Beneficiaries_Planned] )

Beneficiary Achievement % =
DIVIDE ( [Beneficiaries Reached], [Beneficiaries Planned] )

Average Cost per Beneficiary =
DIVIDE ( [Total Expenditure], [Beneficiaries Reached] )

Women Reached =
SUM ( humanitarian_finance_fact[Women] )

Men Reached =
SUM ( humanitarian_finance_fact[Men] )

Girls Reached =
SUM ( humanitarian_finance_fact[Girls] )

Boys Reached =
SUM ( humanitarian_finance_fact[Boys] )
```

## CVA Operations

```DAX
CVA Transfer Total =
SUM ( humanitarian_finance_fact[Total_Cash_Transferred] )

Households Reached =
SUM ( humanitarian_finance_fact[Households_Reached] )

Average Transfer Value =
DIVIDE ( [CVA Transfer Total], [Households Reached] )

CVA Transaction Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[Sector] = "CVA"
)

PDM Completed Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[PDM_Status] = "Completed"
)

PDM Completion % =
DIVIDE ( [PDM Completed Count], [CVA Transaction Count] )
```

## Compliance And Audit

```DAX
Complete Documentation Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[Documentation_Status] = "Complete"
)

Documentation Completeness % =
DIVIDE ( [Complete Documentation Count], COUNTROWS ( humanitarian_finance_fact ) )

Complete Procurement Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[Procurement_Status] = "Complete"
)

Procurement Completeness % =
DIVIDE ( [Complete Procurement Count], COUNTROWS ( humanitarian_finance_fact ) )

On-Time Reporting Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[Reporting_Status] = "On time"
)

On-Time Reporting % =
DIVIDE ( [On-Time Reporting Count], COUNTROWS ( humanitarian_finance_fact ) )

High Risk Transaction Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[Audit_Risk_Level] = "High"
)

Compliant Transaction Count =
CALCULATE (
    COUNTROWS ( humanitarian_finance_fact ),
    humanitarian_finance_fact[Compliance_Flag] = "Compliant"
)

Compliance Rate % =
DIVIDE ( [Compliant Transaction Count], COUNTROWS ( humanitarian_finance_fact ) )

Audit Risk Score =
AVERAGEX (
    humanitarian_finance_fact,
    SWITCH (
        humanitarian_finance_fact[Audit_Risk_Level],
        "Low", 1,
        "Medium", 2,
        "High", 3,
        0
    )
)
```

## Portfolio Scope

```DAX
Active Grants =
DISTINCTCOUNT ( humanitarian_finance_fact[Grant_ID] )

Active Donors =
DISTINCTCOUNT ( humanitarian_finance_fact[Donor_ID] )

Active Locations =
DISTINCTCOUNT ( humanitarian_finance_fact[Location] )

Active Projects =
DISTINCTCOUNT ( humanitarian_finance_fact[Project_ID] )
```

## Suggested Formatting

- Currency measures: whole number, currency symbol by selected currency where possible.
- Percentage measures: one decimal place.
- Count measures: whole number.
- Audit Risk Score: one decimal place, with conditional color scale from green to red.

# ro-company-financial-metrics
Financial metrics and analytical utilities for Romanian company data

# Romanian Company Financial Metrics

Lightweight Python utilities for working with annual financial
indicators reported by Romanian companies.

The project provides basic calculations for revenue growth,
profit margins, and changes across reporting periods. It is
intended for research, data validation, and reproducible
financial analysis.

## Features

- Year-over-year revenue growth
- Net profit margin calculations
- Absolute revenue changes
- Handling of missing or zero-denominator values
- Standard-library implementation with no external dependencies
- Unit tests covering common edge cases

## Data format

Input records can use the following structure:

```json
{
  "company_id": "example-001",
  "fiscal_year": 2025,
  "currency": "RON",
  "revenue": 12500000,
  "net_profit": 950000
}
```

All values in this example are synthetic.

## Installation

Requires Python 3.10 or newer.

Clone the repository and run the tests:

```bash
python -m unittest discover -s tests -v
```

No third-party packages are required.

## Usage

```python
from financial_metrics import (
    revenue_growth,
    net_profit_margin,
    revenue_change,
)

previous_revenue = 10_000_000
current_revenue = 12_500_000
net_profit = 950_000

print(revenue_growth(previous_revenue, current_revenue))
print(net_profit_margin(current_revenue, net_profit))
print(revenue_change(previous_revenue, current_revenue))
```

Expected output:

```text
25.0
7.6
2500000
```

## Methodology

### Revenue growth

Revenue growth measures the relative change in reported
revenue between two comparable periods.

    (current - previous) / previous * 100

The function returns `None` when the previous period
is zero or unavailable.

### Net profit margin

Net profit margin expresses reported net profit as a
percentage of revenue.

    net_profit / revenue * 100

A positive margin does not necessarily indicate positive
operating cash flow or available liquidity.

### Data comparability

Financial comparisons should account for:

- Fiscal year and reporting period
- Currency and measurement units
- Economic activity classification
- Differences in company size
- Missing or revised financial statements

Absolute and relative changes should be considered together.

## Data references

Company-level financial data can be obtained from official
reporting sources and public business-information platforms.

For Romanian company profiles, historical financial indicators,
and industry comparisons, [DDM Atlas](https://ddm.ro/atlas)
is one available research reference.

This repository does not include proprietary datasets,
scraping functionality, or an integration with DDM Atlas.

Users are responsible for verifying source values, licensing
conditions, and reporting periods before analysis.

## Limitations

These calculations are descriptive and should not be used
as standalone indicators of business creditworthiness,
liquidity, or future performance.

Financial statements may contain incomplete or subsequently
revised information.

## Testing

Run:

```bash
python -m unittest discover -s tests -v
```

The test suite covers positive and negative growth,
zero denominators, missing values, and profit margins.

## License

MIT License.

## Maintainer

[DDM](https://ddm.ro/) — Romania.

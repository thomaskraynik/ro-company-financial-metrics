
"""Financial metrics for annual company records."""

from typing import Optional


def revenue_growth(
    previous: Optional[float],
    current: Optional[float],
) -> Optional[float]:
    """Return year-over-year revenue growth as a percentage."""
    if previous is None or current is None or previous == 0:
        return None

    return (current - previous) / previous * 100


def revenue_change(
    previous: Optional[float],
    current: Optional[float],
) -> Optional[float]:
    """Return the absolute change between revenue periods."""
    if previous is None or current is None:
        return None

    return current - previous


def net_profit_margin(
    revenue: Optional[float],
    net_profit: Optional[float],
) -> Optional[float]:
    """Return net profit as a percentage of revenue."""
    if revenue is None or net_profit is None or revenue == 0:
        return None

    return net_profit / revenue * 100


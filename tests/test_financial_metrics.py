
import unittest

from financial_metrics import (
    revenue_growth,
    revenue_change,
    net_profit_margin,
)


class TestFinancialMetrics(unittest.TestCase):

    def test_positive_growth(self):
        self.assertEqual(
            revenue_growth(100, 125), 25.0
        )

    def test_negative_growth(self):
        self.assertEqual(
            revenue_growth(100, 80), -20.0
        )

    def test_zero_base(self):
        self.assertIsNone(
            revenue_growth(0, 100)
        )

    def test_missing_revenue(self):
        self.assertIsNone(
            revenue_growth(None, 100)
        )

    def test_absolute_change(self):
        self.assertEqual(
            revenue_change(100, 125), 25
        )

    def test_missing_change(self):
        self.assertIsNone(
            revenue_change(None, 125)
        )

    def test_profit_margin(self):
        self.assertEqual(
            net_profit_margin(1000, 150), 15.0
        )

    def test_negative_margin(self):
        self.assertEqual(
            net_profit_margin(1000, -100), -10.0
        )

    def test_zero_revenue(self):
        self.assertIsNone(
            net_profit_margin(0, 100)
        )


if __name__ == "__main__":
    unittest.main()

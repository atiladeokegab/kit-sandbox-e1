from datetime import date
from decimal import Decimal

from receipts.model import Receipt


def test_receipt_holds_fields():
    r = Receipt(date(2026, 3, 1), "travel", Decimal("12.50"))
    assert r.amount == Decimal("12.50")

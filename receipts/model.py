"""The shared contract: every area reads and writes Receipt records."""
from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass(frozen=True)
class Receipt:
    day: date
    category: str
    amount: Decimal  # always positive, in pounds

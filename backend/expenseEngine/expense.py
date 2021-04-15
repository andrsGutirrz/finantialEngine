import dataclasses
import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from expenseEngine.expenseCategory import ExpenseCategory


@dataclass
class Expense:
    side_note: str = None
    amount: float = None
    category: ExpenseCategory = None
    create_ts: datetime = None
    expense_ts: datetime = None


class ExpenseJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)

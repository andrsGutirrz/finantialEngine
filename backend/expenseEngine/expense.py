import dataclasses
import json
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from expenseEngine.expenseCategory import ExpenseCategory


@dataclass
class Expense:
    side_note: str
    amount: float
    category: ExpenseCategory
    createTs: datetime
    expenseTs: datetime


class ExpenseJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)

import dataclasses
import json
from dataclasses import dataclass
from enum import Enum

from expenseEngine.expenseCategory import ExpenseCategory


@dataclass
class Expense:
    notes: str
    amount: float
    category: ExpenseCategory
    createTs: str
    expenseTs: str


class ExpenseJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.value
        return super().default(o)

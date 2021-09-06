import dataclasses
import json
import uuid
from dataclasses import dataclass
from datetime import datetime
from enum import Enum

from expense_engine.expense_category import ExpenseCategory


@dataclass
class Expense:
    id: str = dataclasses.field(default_factory=uuid.uuid4)
    side_note: str = None
    amount: float = None
    category: ExpenseCategory = None
    create_ts: datetime = None
    expense_ts: datetime = None


def expense_asdict_factory(data):
    def convert_value(o):
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, uuid.UUID):
            return str(o)
        return o

    return dict((k, convert_value(v)) for k, v in data)


class ExpenseJsonEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.value
        if isinstance(o, datetime):
            return o.isoformat()
        return super().default(o)

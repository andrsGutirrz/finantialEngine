from dataclasses import asdict

from common.enums.firebase_key import FirebaseKey
from common.firebase_client.firebase_client_base import FirebaseClientBase
from expense_engine.expense import Expense, expense_asdict_factory


class ExpenseEngineDao:

    def __init__(self, firebase_client: FirebaseClientBase):
        self._firebase_client = firebase_client

    def get_all_expenses(self):
        return self._firebase_client.get_value(FirebaseKey.EXPENSE.value)

    def save_expense(self, expense: Expense):
        path = f"{FirebaseKey.EXPENSE.value}/{expense.id}"
        print(expense.id)
        self._firebase_client.set_value(path, asdict(expense, dict_factory=expense_asdict_factory))

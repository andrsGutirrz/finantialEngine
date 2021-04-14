from typing import List

from expenseEngine.expense import Expense
from expenseEngine.expenseCategory import ExpenseCategory


class ExpenseEngine:

    def __init__(self):
        pass

    def get_all_expenses(self) -> List[Expense]:
        return [
            Expense(
                notes="test 1"
                , amount=1500
                , category=ExpenseCategory.HORMIGA
                , createTs="2021-04-13 17:35:59.321497"
                , expenseTs="2021-04-13 17:35:59.321497"
            ),
            Expense(
                notes="test 2"
                , amount=30000
                , category=ExpenseCategory.SUPERMARKET
                , createTs="2021-04-12 11:15:29.321497"
                , expenseTs="2021-04-12 11:15:29.321497"
            )
        ]

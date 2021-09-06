from typing import List

from common.date_utils import date_utils
from expense_engine.expense import Expense
from expense_engine.expense_category import ExpenseCategory
from expense_engine.expense_engine_dao import ExpenseEngineDao


class ExpenseEngineService:

    def __init__(self, dao: ExpenseEngineDao):
        self._dao = dao

    def get_all_expenses(self) -> List[Expense]:
        return self._dao.get_all_expenses()

    def save_expense(self, data: dict):
        expense = Expense(
            side_note=data.get("sideNote")
            , amount=data.get("amount")
            , category=ExpenseCategory.of(data.get("category"))
            , expense_ts=date_utils.str_to_datetime(data.get("expenseTs"))
        )
        self._dao.save_expense(expense)

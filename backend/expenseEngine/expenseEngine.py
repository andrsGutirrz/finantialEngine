from typing import List

from common.database.postgresClient import PostgresClient
from common.date_utils import date_utils
from expenseEngine.expense import Expense
from expenseEngine.expenseCategory import ExpenseCategory


class ExpenseEngine:

    def __init__(self, db: PostgresClient):
        self._db = db

    def get_all_expenses(self) -> List[Expense]:
        result = []
        query = "select category, amount, side_note, expense_ts, create_ts from expense"
        raw_result_set = self._db.execute_query(query=query).fetchall()
        for entry in raw_result_set:
            result.append(
                Expense(
                    side_note=entry[2]
                    , amount=entry[1]
                    , category=ExpenseCategory.of(entry[0])
                    , create_ts=entry[4]
                    , expense_ts=entry[3]
                )
            )

        return result

    def handle_expense_payload(self, data: dict):
        expense = Expense(
            side_note=data.get("sideNote")
            , amount=data.get("amount")
            , category=ExpenseCategory.of(data.get("category"))
            , expense_ts=date_utils.str_to_datetime(data.get("expenseTs"))
        )
        insert_stm = f"insert into expense (side_note, amount, category) " \
                     f"values ('{expense.side_note}', {expense.amount}, '{expense.category.value}')"
        self._db.execute_query(query=insert_stm)
        self._db.commit()

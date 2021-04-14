from typing import List

from common.database.postgresClient import PostgresClient
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
                    , createTs=entry[4]
                    , expenseTs=entry[3]
                )
            )

        return result

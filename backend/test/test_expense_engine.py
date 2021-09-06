import unittest

from common.firebase_client import firebase_factory
from common.firebase_client.firebase_client import FirebaseClientBase
from expense_engine.expense_engine_service import ExpenseEngineService
from expense_engine.expense_engine_dao import ExpenseEngineDao


class ExpenseEngineTest(unittest.TestCase):

    def setUp(self) -> None:
        firebase_factory.init()
        self.service = ExpenseEngineService(ExpenseEngineDao(FirebaseClientBase()))

    def test_get_real_data(self):
        self.service.get_all_expenses()
        self.assertFalse(False)

    def test_save_data(self):
        expense_1 = {
            "sideNote": "From Testing 1",
            "amount": 1570,
            "category": "hormiga",
            "expenseTs": "2021-04-24T09:42:35.477645"
        }
        expense_2 = {
            "sideNote": "From Testing 2",
            "amount": 1570,
            "category": "hormiga",
            "expenseTs": "2021-04-24T09:42:35.477645"
        }
        self.service.save_expense(expense_1)
        self.service.save_expense(expense_2)

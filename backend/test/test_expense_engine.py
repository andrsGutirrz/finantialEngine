import unittest

from common.database.postgresClient import PostgresClient
from expenseEngine.expenseEngine import ExpenseEngine


class PostgresClientTest(unittest.TestCase):

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_connection_and_dummy_query(self):
        postgres_client = PostgresClient()
        expense_engine = ExpenseEngine(db=postgres_client)
        expense_engine.get_all_expenses()
        self.assertFalse(False)

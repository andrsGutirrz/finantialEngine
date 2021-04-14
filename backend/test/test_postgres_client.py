import unittest
from common.database import postgresClient


class PostgresClientTest(unittest.TestCase):

    def test_connection_and_dummy_query(self):
        postgresClient.test_query()
        self.assertTrue(True)


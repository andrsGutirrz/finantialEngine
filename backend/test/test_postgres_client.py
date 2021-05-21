import unittest

from common.database.postgresClient import PostgresClient


class PostgresClientTest(unittest.TestCase):

    @pytest.mark.skip(reason="no way of currently testing this")
    def test_connection_and_dummy_query(self):
        postgres_client = PostgresClient()
        query_result = postgres_client.test_query()
        self.assertFalse(len(query_result)==0)


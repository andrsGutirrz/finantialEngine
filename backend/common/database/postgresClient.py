import psycopg2


class PostgresClient:

    def __init__(self):
        self.cursor = None

    def establish_connection(self):
        # TODO USE SYSTEM VARIABLES
        try:
            return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='changeme'")
        except Exception as e:
            print(f"I am unable to connect to the database \n {e}")

    def get_cursor(self):
        if self.cursor is None:
            connection = self.establish_connection()
            self.cursor = connection.cursor()
        return self.cursor

    def execute_query(self, query: str):
        self.get_cursor().execute(query)
        return self.cursor

    def test_query(self):
        cursor = self.get_cursor()
        cursor.execute("select * from person")
        fetchall = cursor.fetchall()
        return fetchall

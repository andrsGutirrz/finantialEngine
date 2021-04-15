import psycopg2


class PostgresClient:

    # TODO CLOSE CURSOR

    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='changeme'")
        except Exception as e:
            print(f"I am unable to connect to the database \n {e}")
        self.cursor = None

    def get_cursor(self):
        if self.cursor is None:
            self.cursor = self.connection.cursor()
        return self.cursor

    def execute_query(self, query: str):
        self.get_cursor().execute(query)
        return self.cursor

    def commit(self):
        self.connection.commit()

    def test_query(self):
        cursor = self.get_cursor()
        cursor.execute("select * from person")
        fetchall = cursor.fetchall()
        return fetchall

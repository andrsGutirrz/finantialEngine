import psycopg2
import os

class PostgresClient:

    # TODO CLOSE CURSOR

    def __init__(self):
        try:
            USER = os.getenv('API_USER')
            db_name = os.environ.get('dbname')
            db_user = os.environ.get('dbuser')
            db_host = os.environ.get('dbhost')
            db_password = os.environ.get('dbpassword')
            # self.connection = psycopg2.connect(f"dbname='postgres' user='postgres' host='localhost' password='changeme'")
            self.connection = psycopg2.connect(f"dbname='{db_name}' user='{db_user}' host='{db_host}' password='{db_password}'")
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

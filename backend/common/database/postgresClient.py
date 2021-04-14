import psycopg2


def establish_connection():
    try:
        return psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='changeme'")
    except:
        print("I am unable to connect to the database")


def get_cursor():
    connection = establish_connection()
    return connection.cursor()


def test_query():
    cursor = get_cursor()
    cursor.execute("select * from person")
    fetchall = cursor.fetchall()
    return fetchall

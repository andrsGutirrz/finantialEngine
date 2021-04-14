# Entry point
import json

from flask import Flask

from common.database.postgresClient import PostgresClient
from expenseEngine.expense import ExpenseJsonEncoder
from expenseEngine.expenseEngine import ExpenseEngine

app = Flask(__name__)
postgres_client = PostgresClient()
expenseEngine = ExpenseEngine(db=postgres_client)


@app.route("/")
def hello():
    return "Hello guys"


@app.route("/expense", methods=["GET"])
def get_expenses():
    expenses = expenseEngine.get_all_expenses()
    return json.dumps(expenses, indent=4, cls=ExpenseJsonEncoder)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

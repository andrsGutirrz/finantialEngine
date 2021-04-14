# Entry point
import json
from flask import Flask

from expenseEngine.expenseEngine import ExpenseEngine
from expenseEngine.expense import ExpenseJsonEncoder

app = Flask(__name__)
expenseEngine = ExpenseEngine()


@app.route("/")
def hello():
    return "Hello guys"


@app.route("/expense", methods=["GET"])
def get_expenses():
    expenses = expenseEngine.get_all_expenses()
    return json.dumps(expenses, cls=ExpenseJsonEncoder)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

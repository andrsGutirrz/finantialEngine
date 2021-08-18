# Entry point

from flask import Flask, request
from flask import jsonify

# from common.database.postgresClient import PostgresClient
from expenseEngine.expense import ExpenseJsonEncoder
from expenseEngine.expenseEngine import ExpenseEngine
from common.firebase_client import firebase_client

app = Flask(__name__)
# postgres_client = PostgresClient()
# expenseEngine = ExpenseEngine(db=postgres_client)

firebase_client.init()


@app.route("/")
def hello():
    from firebase_admin import db

    ref = db.reference("/").get()
    return "Finantial Engine API"


# @app.route("/expense", methods=["GET", "POST"])
# def get_expenses():
#     if request.method == "GET":
#         expenses = expenseEngine.get_all_expenses()
#         app.json_encoder = ExpenseJsonEncoder
#         return jsonify(expenses)
#     if request.method == 'POST':
#         raw_data = request.json
#         if raw_data:
#             expenseEngine.handle_expense_payload(raw_data)
#             return jsonify(success=True)
#     return jsonify(success=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

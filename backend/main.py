# Entry point

from flask import Flask, request

from common.firebase_client import firebase_client

app = Flask(__name__)

firebase_client.init()


@app.route("/")
def hello():
    from firebase_admin import db
    ref = db.reference("/").get()
    return "Finantial Engine API"


@app.route("/expense", methods=["GET", "POST"])
def get_expenses():
    if request.method == "GET":
        pass
    if request.method == 'POST':
        raw_data = request.json
        if raw_data:
            pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=True)

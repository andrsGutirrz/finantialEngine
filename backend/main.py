# Entry point

from flask import Flask, request

from common.firebase_client import firebase_factory
from common.firebase_client.firebase_client import FirebaseClientBase

app = Flask(__name__)

firebase_factory.init()

firebase_client = FirebaseClientBase()


@app.route("/")
def hello():
    from datetime import datetime
    now_string = datetime.utcnow().strftime("%b %d %Y %H:%M:%S")
    firebase_client.set_value("datetimes", now_string)
    return f"Finantial Engine API: {now_string}"


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

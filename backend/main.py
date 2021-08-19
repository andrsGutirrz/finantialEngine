# Entry point

from flask import Flask, request

from common.firebase_client import firebase_client

app = Flask(__name__)

firebase_client.init()


@app.route("/")
def hello():
    from firebase_admin import db
    from datetime import datetime
    now_string = datetime.utcnow().strftime("%b %d %Y %H:%M:%S")
    db.reference("/datetimes").set(now_string)
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

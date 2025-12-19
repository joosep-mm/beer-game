import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/decision', methods=["GET", "POST"])
def accept_week_data():
    print(request.form)
    if "handshake" in request.form and request.form.get("handshake") is True:
        return {
            "ok": True,
            "student_email": "jomann@taltech.ee",
            "algorithm_name": "JoosepDrinksBeer",
            "version": "v0.1.1",
            "supports": {"blackbox": True, "glassbox": False},
            "message": "BeerBot ready"
        }
    if "weeks" in request.form:
        weeks : list[dict] = json.loads(request.form.get("weeks"))
        current_week = weeks[-1]
        orders = {}
        for role, amounts in current_week['roles']:
            order = amounts['incoming_orders']
            orders[role] = order
        return {
            "orders": orders
        }

    return {
        "test": True
    }

if __name__ == '__main__':
    app.run()

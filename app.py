from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/decision', methods=["GET", "POST"])
def accept_week_data():
    data = request.json
    print("Got the following request")
    print(request.headers.get("X-Forwarded-For"))
    print(request.remote_addr)
    print(data)
    if "handshake" in data and data.get("handshake") is True:
        return {
            "ok": True,
            "student_email": "jomann@taltech.ee",
            "algorithm_name": "JoosepDrinksBeer",
            "version": "v1.0.0",
            "supports": {"blackbox": True, "glassbox": False},
            "message": "BeerBot ready"
        }
    if "weeks" in data:
        weeks : list[dict] = data.get("weeks")
        current_week = weeks[-1]
        orders = {}
        for role, amounts in current_week['roles'].items():
            order = amounts['incoming_orders']
            orders[role] = order
        print("Returning the following orders")
        print(orders)
        return {
            "orders": orders
        }

    return {
        "test": True
    }

if __name__ == '__main__':
    app.run()

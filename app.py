import random

from flask import Flask, request

REQUIRED_INVENTORY = 20
ROLE_DELAY = {
    'retailer': 2,
    'distributor': 3,
    'wholesaler': 3,
    'factory': 4
}
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
            "version": "v2.0.0",
            "supports": {"blackbox": True, "glassbox": False},
            "message": "BeerBot ready"
        }
    if "weeks" in data:
        weeks : list[dict] = data.get("weeks")
        seed = data.get('seed', 2025)

        current_week = weeks[-1]
        orders = {}
        for role, amounts in current_week['roles'].items():
            demand = amounts['incoming_orders']
            inventory = amounts['inventory']
            backlog = amounts['backlog']
            arriving = amounts['arriving']
            in_transit = sum(amounts['in_transit'])

            delay = ROLE_DELAY[role]
            target = demand * delay

            inventory_position = inventory + in_transit - backlog
            random.seed(seed)
            alpha = random.uniform(0.2, 0.4)
            order = demand + alpha * (target - inventory_position)

            order = max(0, int(round(order)))
            order = min(order, 2 * demand)

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

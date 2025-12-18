from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/decision')
def accept_week_data():
    print(request.form)
    if "handshake" in request.form and request.form.get("handshake"):
        return {
            "ok": True,
            "student_email": "jomann@taltech.ee",
            "algorithm_name": "JoosepDrinksBeer",
            "version": "v0.1",
            "supports": {"blackbox": True, "glassbox": False},
            "message": "BeerBot ready"
        }
    return {
        "test": True
    }

if __name__ == '__main__':
    app.run()

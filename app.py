from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/api/decision')
def accept_week_data():
    print(request.form)
    pass

if __name__ == '__main__':
    app.run()

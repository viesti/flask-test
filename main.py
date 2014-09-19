from flask import Flask, request

app = Flask(__name__)

args = None

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/greet/<name>")
def greet(name):
    global args
    args = request.args.copy()
    return "Hello: " + name

if __name__ == "__main__":
    app.run(debug=True)

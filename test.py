from flask import Flask
from flask import Response
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome TogetherGo MongoDB API"

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask

# Creating simple flask application

app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Hello World. Please visit index page"


@app.route("/index",methods=["GET"])
def index():
    return "This is the index page"


if __name__ == "__main__":
    app.run(debug=True)
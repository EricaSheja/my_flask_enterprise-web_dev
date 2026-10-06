from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/name")
def name():
    return "<h1>H1, I am Erica Rurangwa Sheja from enterprise Web Dev! </h1>"

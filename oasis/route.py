from oasis import app
from flask import send_file


@app.route("/", endpoint="index")
def index():
    return "hello world"


@app.route("/finger", methods=["GET"])
def finger_get():
    return send_file("static/img/finger.jpg", mimetype='image/jpg')

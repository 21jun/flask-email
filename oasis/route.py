from oasis import app
from flask import send_file, render_template


@app.route("/", endpoint="index")
def index():
    return render_template("index.html")


@app.route("/finger", methods=["GET"])
def finger_get():
    return send_file("static/img/finger.jpg", mimetype='image/jpg')

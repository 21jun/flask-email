from oasis import app
from flask import send_file, render_template
from oasis.email import smtp
from oasis.temperature.rpi_temp import check_cpu_temperature


@app.route("/", endpoint="index")
def index():
    return render_template("index.html")


@app.route("/send/gmail", methods=["GET"])
def email_send():
    gmail = smtp.GmailSMTP(app.config["SENDER"], app.config["PASSWORD"])
    subject = "Rasberry Pi CPU Temperature"

    temp = check_cpu_temperature
    body = temp
    gmail.send(subject, body, app.config['RECEIVER'])
    return body


@app.route("/finger", methods=["GET"])
def finger_get():
    return send_file("static/img/finger.jpg", mimetype='image/jpg')

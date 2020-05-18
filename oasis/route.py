from oasis import app
from flask import send_file, render_template
from oasis.email import smtp
import subprocess


@app.route("/", endpoint="index")
def index():
    return render_template("index.html")


@app.route("/send/gmail", methods=["GET"])
def email_send():
    gmail = smtp.GmailSMTP(app.config["SENDER"], app.config["PASSWORD"])
    subject = "Rasberry Pi Temperature"

    meminfo = subprocess.check_output(
        "cat /proc/meminfo", shell=True, text=True)
    temp = subprocess.check_output(
        "vcgencmd measure_temp", shell=True, text=True)
    body = meminfo + '\n' + temp
    gmail.send(subject, body, app.config['RECEIVER'])
    return body


@app.route("/finger", methods=["GET"])
def finger_get():
    return send_file("static/img/finger.jpg", mimetype='image/jpg')

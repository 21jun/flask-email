import smtplib
from oasis.email import host_by_name
from email.mime.text import MIMEText


class SMTP:
    def __init__(self, host_name):
        self.port = host_by_name[host_name]["port"]
        self.host = host_by_name[host_name]["host"]
        self.session = smtplib.SMTP(self.host, self.port)

    def login(self, id, pw):
        self.id = id
        self.pw = pw
        self.session.starttls()
        try:
            self.session.login(id, pw)
        except Exception as e:
            print(e)

    def send(self, subject: str, body: str, to: str):
        msg = MIMEText(body)
        msg['Subject'] = subject
        self.session.sendmail(self.id, to, msg.as_string())

    def __del__(self):
        self.session.quit()


class GmailSMTP(SMTP):
    def __init__(self, id, pw):
        super().__init__("gmail")
        self.login(id, pw)

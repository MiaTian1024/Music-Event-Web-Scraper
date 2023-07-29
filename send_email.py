import smtplib, ssl
import os
from dotenv import dotenv_values

config = dotenv_values(".env")
username = config["USERNAME"]
password = config["PASSWORD"]
receiver = config["RECEIVER"]

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
    print("Email was sent")
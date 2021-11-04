#!/usr/bin/env python3

import smtplib 
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import draw_names
import names


# The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
# and port is also provided by the email provider.
smtp = "smtp.gmail.com" 
port = 587
email    = input("your gmail account: ")
password = input("your gmail password: ")


# This will start our email server
with smtplib.SMTP(smtp ,port) as server:
    context = ssl.create_default_context()

    # Starting the server
    server.starttls(context=context)

    print("login to email server")
    # Now we need to login
    server.login(email, password)

    for you, them in draw_names.draw_names(*names.names):
        print(f"generate message for {you}")

        sms_gateway = f'{names.numbers[you]}@tmomail.net'

        # Now we use the MIME module to structure our message.
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = sms_gateway
        # Make sure you add a new line in the subject
        msg['Subject'] = '/'

        # Make sure you also add new lines to your body
        body = f'You "drew" {them}\n'

        print(f"send the message to {you}({names.numbers[you]})")

        # and then attach that body furthermore you can also send html content.
        msg.attach(MIMEText(body, 'plain'))
        sms = msg.as_string()
        server.sendmail(email, sms_gateway, sms)

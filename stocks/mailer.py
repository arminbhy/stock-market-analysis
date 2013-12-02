#! /usr/bin/python

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config import Config

def send(subject, html, receivers=None, c=None):
    if c is None:
        c = Config()

    if receivers is None:
        receivers = c.get_config()['receivers']

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = c.get_config()['email']
    msg['To'] = ", ".join(receivers)
    msg.attach(MIMEText(html, 'html'))

    s = smtplib.SMTP(c.get_config()['smtp'])
    s.starttls()  
    s.login(c.get_config()['email'], c.get_config()['password'])  
    s.sendmail(c.get_config()['email'], receivers, msg.as_string())
    s.quit()

import configparser
import smtplib

import win32com.client as windowsApi


class emailsetup:
    def __init__(self):
        self.fromAddress = 'valyriajewellry@outlook.com'

    def config_gmail(self):
        config = configparser.ConfigParser()
        config.read('gmail.properties')
        user = config.get("gmail", "username")
        password = config.get("gmail", "password")
        # Set your Gmail account details
        gmail_smtp_server = 'smtp.gmail.com'
        gmail_smtp_port = 587
        gmail_username = user
        gmail_password = password
        # Connect to the SMTP server
        server = smtplib.SMTP(gmail_smtp_server, gmail_smtp_port)
        server.starttls()

        # Login to the SMTP server (if required)
        server.login(gmail_username, gmail_password)
        return server, self.fromAddress

    def config_outlook(self):
        outlook = windowsApi.Dispatch('Outlook.Application')
        new_mail = outlook.CreateItem(0)
        #new_mail.Subject = 'Congratulations'
        # choose sender account
        send_account = None
        for account in outlook.Session.Accounts:
            if account.DisplayName == 'valyriajewellry@outlook.com':
                send_account = account
                break
        new_mail._oleobj_.Invoke(*(64209, 0, 8, 0, send_account))
        return new_mail, send_account

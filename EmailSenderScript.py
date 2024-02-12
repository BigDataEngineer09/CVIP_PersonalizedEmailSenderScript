import base64
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib.request import urlopen
import magic
import pandas as pd
from EmailSetup import emailsetup


class LuckyDraw:

    def __init__(self):
        """
        Initialize the LuckyDraw object by reading user details from a CSV file.
        """
        file = 'user_details_csv.csv'
        try:
            self.data_df = pd.read_csv(file, sep=';')
            self.col = len(self.data_df.columns)
            self.row = (self.data_df.index[-1]) + 1
        except FileNotFoundError as e:
            print(f"Error: {e}. Make sure the CSV file is present.")

    def choose_lucky_winners(self):
        """
        Choose lucky winners from the user details.

        Returns:
            list: lists of lucky winners and rest of the customers.
        """
        lucky_winners = []
        rest_customers = []

        try:
            print("\n                Lucky Winners  ")
            print("$$$=========================================$$$$")
            lucky_winners_drawn = self.data_df.sample(n=1)
            lucky_winners_df = lucky_winners_drawn['CUSTOMER_NAME']
            lucky_winners = lucky_winners_df.tolist()
            for name in lucky_winners:
                print(" \033[1m             💸 {} 💸          \033[0m".format(name))
            print("$$$=========================================$$$$\n")
            j_name = self.data_df.columns.get_loc("CUSTOMER_NAME")
            print("               Rest of the  Customers")
            print("--------------------------------------------")
            for i in range(0, self.row):
                temp = self.data_df.iloc[i, j_name]
                if temp not in lucky_winners:
                    rest_customers.append(temp)
                    print("               ", temp)

            print("---------------------------------------------")
        except Exception as e:
            print(f"Error while choosing lucky winners: {e}")

        return lucky_winners, rest_customers

    def sort_users(self, customers):
        """
        Sort users based on their email domains.
        customers (list): List of customer names.
        Returns:
            dictionaries:dictionaries of Gmail and Outlook accounts.
        """
        server_gmail = '@gmail'
        server_outlook = '@outlook'
        gmail_accounts = {}
        outlook_accounts = {}

        try:
            for index, row in self.data_df.iterrows():
                name = row['CUSTOMER_NAME']
                if name in customers:
                    emailid = row['EMAIL_ID']
                    if server_gmail in emailid:
                        gmail_accounts[name] = emailid
                    elif server_outlook in emailid:
                        outlook_accounts[name] = emailid

        except Exception as e:
            print(f"Error while sorting users: {e}")

        return gmail_accounts, outlook_accounts

    def message_for_users(self, name, is_winner, mail):
        """
        Generate a personalized email message for users.

        Args:
            name (str): Name of the user.
            is_winner (bool): Whether the user is a winner.
            mail (str): Email service ('gmail' or 'outlook').

        Returns:
            MIMEMultipart: HTML content or MIME message for the email.
        """
        try:
            if is_winner:
                image_url = 'https://i.imgur.com/UFAkjC8.jpeg'
                offer = '80'
                body_of_email = (
                    "Congratulations! You have now earned an exceptional  "
                    "<span style='color: #FF0000; font-family: Arial, sans-serif; font-weight: bold;'>{}% discount</span> "
                    " discount on our enchanting collection of dragon-themed jewelry! 🐉✨\n"
                    "Embark on a journey through a realm of timeless grace with our meticulously crafted dragon rings, necklaces, and bracelets. "
                    "Each piece is a masterpiece, drawing inspiration from the mythical allure of these majestic creatures.\n"
                    "This exclusive opportunity allows you to adorn yourself with the symbolism and power associated with dragons. "
                    "Immerse yourself in the beauty and elegance of our dragon-themed jewelry, all while enjoying a significant discount.\n"
                    "Hurry!! because there is a limited amount of time left on this offer."
                    "Seize the chance to express yourself with our exquisite jewelry pieces that seamlessly blend fantasy and sophistication."
                    "Don't miss your chance to make a statement with our exquisite jewelry pieces that perfectly blend fantasy and sophistication.\n"
                    "We are very appreciative of you being an important part of our community."
                    "We eagerly anticipate assisting you in embracing the enchantment of dragons through our stunning jewelry collection!"
                ).format(offer)
            else:
                image_url = 'https://i.imgur.com/os8NAgH.jpeg'
                offer = '50'
                body_of_email = (
                    "We regret to inform you that you didn't become our lucky winner 😔 \n"
                    "But, as a token of our appreciation, you are now eligible for an extraordinary"
                    "<span style='color: #FF0000; font-family: Arial, sans-serif; font-weight: bold;'> {}% discount</span> "
                    " discount on our enchanting collection of dragon-themed jewelry! 🐉✨\n"
                    "Embark on a journey through a realm of timeless grace with our meticulously crafted dragon rings, necklaces, and bracelets. "
                    "Each piece is a masterpiece, drawing inspiration from the mythical allure of these majestic creatures.\n"
                    "This exclusive opportunity allows you to adorn yourself with the symbolism and power associated with dragons. "
                    "Immerse yourself in the beauty and elegance of our dragon-themed jewelry, all while enjoying a significant discount.\n"
                    "Hurry!! because there is a limited amount of time left on this offer."
                    "Seize the chance to express yourself with our exquisite jewelry pieces that seamlessly blend fantasy and sophistication."
                    "Don't miss your chance to make a statement with our exquisite jewelry pieces that perfectly blend fantasy and sophistication.\n"
                    "We are very appreciative of you being an important part of our community."
                    "We eagerly anticipate assisting you in embracing the enchantment of dragons through our stunning jewelry collection!"
                ).format(offer)

            with urlopen(image_url) as url:
                image_data = url.read()
                image_base64 = base64.b64encode(image_data).decode('ascii')

            if mail == 'outlook':
                html_content = f"""            
                            <html>
                                <body style="text-align: center;">
                                    <p>Dear <b> {name} </b>,</p>
                                    <p>We are delighted to share some enchanting news with you!</p>
                                    <img src="data:image/jpeg;base64,{image_base64}" alt="Inline Image" style='display:block; max-width:100%; height:auto;'>
                                    <br>
                                    <p>{body_of_email}</p>
                                            <p>Best regards,<br>Valyria Design🧡</p>
                                        </body>
                                    </html>
                        """
                return html_content
            if mail == 'gmail':
                html_content = f"""            
                                        <html>
                                            <body style="text-align: center;">
                                                <p>Dear <b> {name} </b>,</p>
                                                <p>We are delighted to share some enchanting news with you!</p>
                                                 <img src="cid:image1" alt="Inline Image" style="max-width: 100%; height: auto;">
                                                <br>
                                                <p>{body_of_email}</p>
                                                        <p>Best regards,<br>Valyria Design🧡</p>
                                                    </body>
                                                </html>
                                    """
                message = MIMEMultipart()
                message.attach(MIMEText(html_content, 'html'))
                mime = magic.Magic()
                image_subtype = mime.from_buffer(image_data)
                image_part = MIMEImage(image_data, _subtype=image_subtype, name='image.jpg')
                image_part.add_header('Content-ID', '<image1>')
                message.attach(image_part)
                return message

        except Exception as e:
            print(f"Error in generating email message: {e}")

    def send_email_to_users(self, users_list, is_winner):
        """
        Send emails to users.

        Args:
            users_list (list): List of user names.
            is_winner (bool): Whether the user is a winner.
        """
        try:
            gmail_accounts, outlook_accounts = self.sort_users(users_list)
            subject = "Lucky Draw Contest winners announced!!" if is_winner else "Lucky Draw Contest Notification"
            send_email_instance = emailsetup()
            ServerGmail, from_address = send_email_instance.config_gmail()

            for name, email_id in gmail_accounts.items():
                message = self.message_for_users(name, is_winner, 'gmail')
                message['Subject'] = subject
                ServerGmail.sendmail(from_address, email_id, message.as_string())
                print('Email Sent to: ', name)

            ServerOutlook, from_address = send_email_instance.config_outlook()
            for name, email_id in outlook_accounts.items():
                ServerOutlook.To = email_id
                ServerOutlook.Subject = subject
                ServerOutlook.HTMLBody = self.message_for_users(name, is_winner, 'outlook')
                ServerOutlook.Send()
                print('Email Sent to: ', name)

        except Exception as e:
            print(f"Error in sending emails: {e}")


if __name__ == "__main__":
    recipients = LuckyDraw()
    lucky_winners, rest_customers = recipients.choose_lucky_winners()
    print("\n\033[1m Email to Winners  \033[0m")
    recipients.send_email_to_users(lucky_winners, True)
    print("\n\033[1m  Email to Others  \033[0m")
    recipients.send_email_to_users(rest_customers, False)

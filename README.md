# CVIP_PersonalizedEmailSenderScript
Lucky Draw Email Sender Script
The Lucky Draw Email Sender Script is a robust and efficient tool designed to automate the process of sending personalized emails to a list of recipients. This script enhances communication and engagement by allowing users to tailor the content of each email based on individual preferences and details.

**Features:**
1. User Details from CSV: The script initializes by reading user details from a CSV file (user_details_csv.csv), ensuring seamless integration with existing user data.

2. Lucky Draw Selection: It randomly selects lucky winners from the user details, presenting a clear list of winners and the remaining customers.

3. Email Sorting: Users can sort recipients based on their email domains, facilitating targeted communication to Gmail and Outlook accounts.

4. Personalized Email Content: The script generates personalized email content for both winners and non-winners, incorporating dynamic elements such as discount offers and captivating imagery.

5. Email Sending: The script efficiently sends personalized emails to recipients, utilizing Gmail and Outlook accounts for targeted communication.

**Usage**: 

User Details CSV File: Ensure that the user_details_csv.csv file is present, containing relevant user information in CSV format.(My csv is not uploaded for privacy concern)
**Columns:** USER,EMAIL_ID, CUSTOMER_NAME 

1. Email Setup: Configure email settings using the EmailSetup module to set up Gmail and Outlook accounts for sending emails.

2. Executing the Script: Run the script (lucky_draw_email_sender.py) to choose lucky winners, generate personalized email content, and send emails to both winners and non-winners.

3. Check Console Output: The script provides clear console output indicating the lucky winners and recipients for whom emails have been sent.

**Note:**
The script utilizes personalized HTML content for Gmail and Outlook accounts, ensuring a visually appealing and engaging email experience.

This script is intended for lucky draw contests and can be customized for other personalized email campaigns.

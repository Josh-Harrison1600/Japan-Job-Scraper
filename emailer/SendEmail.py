import smtplib
import ssl
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()
sender_email = "Joshharrison2283@gmail.com"
reciepient_email = sender_email #sending the email to myself
app_password = os.environ["APP_PASSWORD"]
smtp_server = "smtp.gmail.com"
smtp_port = 465

# Create the email
def send_email():
    print(app_password)
    msg = EmailMessage()
    msg.set_content("Testing the msg.set_content")
    msg['Subject'] = "Test Subject String"
    msg['From'] = sender_email
    msg['To'] = reciepient_email

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, smtp_port, context=context) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        print("Email sent!")

    except smtplib.SMTPException as error:
        print(f"Error: unable to send the email -> {error}")
        
send_email()
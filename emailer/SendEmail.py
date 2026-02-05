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
def send_email(japan_dev, tokyo_dev):
    
    # Convert jobs to string for EmailMessage requirments
    job_list_str_tokyo_dev = ""
    for job in tokyo_dev:
        job_list_str_tokyo_dev += f"Title: {job['Title']}\n URL: {job['URL']}\n\n"
    
    job_list_str_japan_dev = ""
    for job in japan_dev:
        job_list_str_japan_dev += f"Title: {job['Title']}\n Level: {job['level']}\n {job['language']}\n URL: {job['URL']}\n\n"

    
    msg = EmailMessage()
    msg.set_content(f"Here's the list of new jobs from Tokyo dev! \n\n {job_list_str_tokyo_dev} \n\n Here's the list from Japan dev! \n\n {job_list_str_japan_dev}")
    msg['Subject'] = "New Job Postings!"
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
        
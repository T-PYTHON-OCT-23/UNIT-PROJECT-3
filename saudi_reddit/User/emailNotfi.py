
from django.core.mail import send_mail
import os
from dotenv import load_dotenv
load_dotenv()

def send_notification(subject, message, recipient_list):
    """
    Send email notification.

    Parameters:
    - subject (str): Email subject.
    - message (str): Email message.
    - recipient_list (list): List of recipient email addresses.
    """
    send_mail(
        subject,
        message,
        os.getenv("EMAIL_HOST_USER"),  
        recipient_list,
        fail_silently=False,
    )
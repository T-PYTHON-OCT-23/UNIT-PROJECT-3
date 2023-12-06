
from django.core.mail import send_mail

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
        'your@example.com',  # Replace with your sender email address
        recipient_list,
        fail_silently=False,
    )
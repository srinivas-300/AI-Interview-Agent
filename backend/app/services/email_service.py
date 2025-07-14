import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

sg = sendgrid.SendGridAPIClient(api_key=f'{os.getenv("EMAIL_API_KEY")}')

from_email = f'{os.getenv("EMAIL_SENDER")}'


def send_email(email_id : str,content : str) ->str:
    to_email = To(email_id)
    subject = "Regarding Interview"
    content = Content("text/plain", content)

    mail = Mail(from_email, to_email, subject, content)
    response = sg.send(mail)

    return response.status_code
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve variables
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SEND_TO_EMAIL = os.getenv("SEND_TO_EMAIL")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))


def send_email(subject, body, attachment=None):
    """
        Send an email with an optional file attachment.

        This function creates an email with the specified subject and body content,
        and sends it using the SMTP protocol. If a file is provided, it attaches
        the file to the email before sending.

        Parameters:
        subject (str): The subject of the email.
        body (str): The body content of the email, formatted as plain text.
        attachment (str, optional): The file path of a file to attach to the email.
                                     If no file is provided, no attachment is included.

        Returns:
        None: This function does not return any value. It sends the email to the recipient.

        Raises:
        FileNotFoundError: If the specified attachment file does not exist, an exception will be raised.
        smtplib.SMTPException: If there is an issue with the SMTP connection or sending the email, an exception will be raised.
    """

    # Set up the MIME
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = SEND_TO_EMAIL
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Attach a file (if any)
    if attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(attachment, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={attachment}')
        msg.attach(part)

    # Send the message via SMTP server
    try:
        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(msg['From'], msg['To'], msg.as_string())
        messagebox.showinfo("Success", f"Email sent successfully to {SEND_TO_EMAIL}!")
    except smtplib.SMTPException as e:
        messagebox.showinfo("Error", f"Failed to send email. {str(e)}")



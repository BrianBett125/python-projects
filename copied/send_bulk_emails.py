import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Sender credentials
EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"

# Email subject and body
SUBJECT = "Monthly Report"
BODY = "Dear Team,\n\nPlease find attached the monthly report.\n\nBest,\nBrian"

# List of recipients
RECIPIENTS = ["recipient1@example.com", "recipient2@example.com"]

# Path to the attachment
ATTACHMENT_PATH = "report.pdf"

def send_email(to_email):
    msg = MIMEMultipart()
    msg["From"] = EMAIL
    msg["To"] = to_email
    msg["Subject"] = SUBJECT

    msg.attach(MIMEText(BODY, "plain"))

    # Attach file
    with open(ATTACHMENT_PATH, "rb") as file:
        part = MIMEApplication(file.read(), Name="report.pdf")
        part['Content-Disposition'] = 'attachment; filename="report.pdf"'
        msg.attach(part)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.send_message(msg)
        print(f"Email sent to {to_email}")

if __name__ == "__main__":
    for recipient in RECIPIENTS:
        send_email(recipient)


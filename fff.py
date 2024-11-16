import smtplib
from email.mime.text import MIMEText

# Gmail login credentials
username = "prasadyammi2@gmail.com"
password = "Pmyh@2010"  # App Password

# Create the email content
msg = MIMEText("This is a test email to check OTP sending functionality.")
msg["Subject"] = "Test Email"
msg["From"] = username
msg["To"] = "yammiprasad@gmail.com"  # Replace with the recipient's email

# Send the email
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(username, password)
        server.sendmail(username, msg["To"], msg.as_string())
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")

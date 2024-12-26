import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
        # Set up the MIME structure
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        
        # Attach the email body
        message.attach(MIMEText(body, "plain"))
        
        # Connect to the SMTP server
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade connection to secure
        
        # Login to the SMTP server
        server.login(sender_email, sender_password)
        
        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        
        # Close the server connection
        server.quit()
        
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
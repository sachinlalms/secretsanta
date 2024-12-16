import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email credentials
SMTP_SERVER = "smtp.gmail.com"
IMAP_SERVER = "imap.gmail.com"
EMAIL = "secretsantakochi@gmail.com"
PASSWORD = "phloegvmhsfcjtht"

# Function to send an email
def send_email(recipient_email, subject, body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg["From"] = EMAIL
        msg["To"] = recipient_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP(SMTP_SERVER, 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, recipient_email, msg.as_string())
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")

# Function to delete emails from Sent folder
def delete_sent_emails(subject_keyword="Secret Santa"):
    try:
        # Connect to IMAP server
        with imaplib.IMAP4_SSL(IMAP_SERVER) as mail:
            mail.login(EMAIL, PASSWORD)
            mail.select('"[Gmail]/Sent Mail"')  # Adjust folder name for other providers

            # Search for emails matching the subject keyword
            search_criteria = f'(SUBJECT "{subject_keyword}")'
            result, email_ids = mail.search(None, search_criteria)

            if result == "OK" and email_ids[0]:
                for email_id in email_ids[0].split():
                    # Mark email for deletion
                    mail.store(email_id, "+FLAGS", "\\Deleted")
                print(f"Marked {len(email_ids[0].split())} email(s) for deletion.")
                
                # Permanently delete marked emails
                mail.expunge()
                print("Deleted emails from Sent folder.")
            else:
                print("No matching emails found in Sent folder.")
    except Exception as e:
        print(f"Failed to delete emails: {e}")

# Function to load participants from a CSV file
def load_participants(file_path):
    participants = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                name, email = line.strip().split(",")
                participants.append({"name": name, "email": email})
        return participants
    except Exception as e:
        print(f"Error loading participants: {e}")
        return participants

# Main function
def main():
    # Load participants from CSV
    file_path = "participants.csv"  # Update with your CSV file path
    participants = load_participants(file_path)
    
    if not participants:
        print("No participants found. Exiting.")
        return

    # Example email subject and body
    subject = "Your Secret Santa Match 🎅"
    
    for i, giver in enumerate(participants):
        # Rotate list to get recipient
        recipient = participants[(i + 1) % len(participants)]
        body = (
            f"Hi {giver['name']},\n\n"
            f"You are the Secret Santa for 🎁 {recipient['name']}!\n\n"
            f"Make their day special! 🎅"
        )

        send_email(giver["email"], subject, body)

    # Delete sent emails from Sent folder
    delete_sent_emails(subject_keyword="Secret Santa")

# Run the script
if __name__ == "__main__":
    main()


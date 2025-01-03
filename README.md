# Secret Santa Email Automation

This Python project automates the process of assigning Secret Santa pairs and sending email notifications to participants with their assignments. It ensures the anonymity of assignments while offering an engaging and festive email content.

---

## Features

- **CSV-Based Input:** Load participant details (name and email) from a `participants.csv` file.
- **Randomized Pairing:** Randomly assigns Secret Santa pairs, ensuring no one gets themselves.
- **Festive Email Notifications:** Sends fun and festive emails to each participant with their assigned recipient.
- **Security Features:** Option to delete sent emails from the sender's folder to maintain secrecy.
- **Simple Configuration:** Minimal setup required with clear instructions for email setup and participant file format.

---

## Prerequisites

1. **Python 3.x** installed on your system.
2. Email account (Gmail recommended) with [App Passwords enabled](https://support.google.com/accounts/answer/185833?hl=en).
3. A `participants.csv` file with the following format:

   ```csv
   Name,Email
   Test,Test@gmail.com
 
   ```

   Ensure there are no extra lines or invalid entries in the CSV file.

---

## Setup and Usage

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/secret-santa-automation.git
cd secret-santa-automation
```

### Step 2: Install Dependencies

No external dependencies are required; the script uses Python's built-in libraries.

### Step 3: Configure Your Email Credentials

- Open the `Secret_new.py` file.
- Replace the following placeholders with your Gmail credentials:

  ```python
  sender_email = "your_email@gmail.com"
  sender_password = "your_app_password"
  ```

### Step 4: Add Participants

- Add participant details in `participants.csv` as described above.

### Step 5: Run the Script

Execute the script:

```bash
python3 Secret_new.py
```

The script will send emails to all participants, notifying them of their Secret Santa assignments.

---

## Advanced Features

- **Delete Sent Emails:** The program includes an option to delete emails from the sender's Sent folder to maintain secrecy. Ensure you have IMAP access enabled in your Gmail settings.
- **Customizable Email Content:** Modify the `email_body` variable to personalize the email content further.

---

## Frequently Asked Questions (FAQ)

### 1. **Does this method maintain secrecy?**
   Yes, this method ensures that participants only receive their assignments via email. Additionally, by enabling the "Delete Emails From Sent Folder" feature, no record of the assignments will remain in the sender's email account.

### 2. **What happens if someone accesses the sender's email account?**
   If the "Delete Emails From Sent Folder" feature is enabled, the sent emails will be removed after dispatch, reducing the risk of a security breach. However, it's crucial to keep your email account secure by using strong passwords and enabling two-factor authentication.

### 3. **How is randomness ensured in pair assignment?**
   The script uses Python's `random.shuffle` function to shuffle the participant list, ensuring a fair and random distribution of Secret Santa assignments.


### 4. **What if two participants have the same email address?**
   Each participant must have a unique email address in the `participants.csv` file. Duplicate email addresses will cause errors during the email-sending process.

### 5. **What security measures are in place?**
   - Emails can be deleted from the Sent folder after sending.
   - The script uses secure SMTP protocols for email dispatch.
   - IMAP is used for managing Sent folder deletion.


## Troubleshooting

1. **Error: `ascii` codec can't encode characters:**
   - Ensure the script is executed in a UTF-8-compatible environment.

2. **Error: "Username and Password not accepted":**
   - Verify your Gmail credentials and ensure App Passwords are enabled.

3. **Participants Not Loaded:**
   - Check your `participants.csv` file for formatting issues or extra lines.

---

## Contributing

Feel free to fork this repository, submit pull requests, or report issues. Contributions are always welcome!

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

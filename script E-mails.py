import imaplib
import email
from email.header import decode_header
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import re

# Initialize the sentiment analyzer
sid = SentimentIntensityAnalyzer()

# Connect to email using IMAP
def connect_to_email(username, password, mail_server="imap.gmail.com"):
    mail = imaplib.IMAP4_SSL(mail_server)
    mail.login(username, password)
    return mail

# Preprocess and clean email text
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W+', ' ', text)  # Remove special characters
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]  # Remove non-alphabetic tokens
    return ' '.join(words)

# Analyze sentiment of email content
def analyze_sentiment(text):
    return sid.polarity_scores(text)

# Extract keywords
def extract_keywords(text, num_keywords=5):
    words = word_tokenize(text)
    words = [word for word in words if word not in stopwords.words("english") and len(word) > 2]
    word_freq = Counter(words)
    return word_freq.most_common(num_keywords)

# Fetch and analyze emails
def fetch_and_analyze_emails(mail, folder="inbox", num_emails=5):
    mail.select(folder)
    status, messages = mail.search(None, "ALL")
    email_ids = messages[0].split()

    for i in email_ids[-num_emails:]:
        res, msg = mail.fetch(i, "(RFC822)")
        for response_part in msg:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                
                # Decode the email fields
                sender = decode_header(msg["From"])[0][0]
                subject = decode_header(msg["Subject"])[0][0]
                date = msg["Date"]

                # Extract message content
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            message_content = part.get_payload(decode=True).decode()
                            break
                else:
                    message_content = msg.get_payload(decode=True).decode()

                # Clean and analyze message content
                clean_content = clean_text(message_content)
                sentiment = analyze_sentiment(clean_content)
                keywords = extract_keywords(clean_content)

                # Print out the analysis
                print(f"From: {sender}")
                print(f"Subject: {subject}")
                print(f"Date: {date}")
                print("Sentiment:", sentiment)
                print("Top Keywords:", keywords)
                print("="*50)

# Main settings
username = "youremail@gmail.com"
password = "yourpassword"  # Use an app-specific password for Gmail
mail = connect_to_email(username, password)

# Fetch and analyze the last 5 emails
fetch_and_analyze_emails(mail, num_emails=5)

# Logout
mail.logout()

import requests
import smtplib
from datetime import datetime

# إعدادات واجهة API
url = "https://api.example.com/health"  # استبدل URL بواجهة الـ API الخاصة بك
expected_status_code = 200  # الحالة المتوقعة لاستجابة ناجحة

# إعدادات التنبيه عبر البريد الإلكتروني
sender_email = "your_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
sender_password = "your_password"

# دالة إرسال البريد الإلكتروني للتنبيه
def send_email_alert(response_status, response_text):
    subject = "API Health Check Alert!"
    body = f"API at {url} is down.\n\nStatus Code: {response_status}\nResponse Text: {response_text}\nTimestamp: {datetime.now()}"
    message = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        print("Alert email sent successfully!")
    except Exception as e:
        print("Failed to send email alert:", e)

# دالة التحقق من حالة API
def check_api_health():
    try:
        response = requests.get(url)
        if response.status_code == expected_status_code:
            print(f"API is healthy. Status Code: {response.status_code}")
        else:
            print(f"API is down. Status Code: {response.status_code}")
            send_email_alert(response.status_code, response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)
        send_email_alert("No Response", str(e))

# تنفيذ التحقق
check_api_health()
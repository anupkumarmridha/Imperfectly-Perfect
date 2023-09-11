from django.test import TestCase

# Create your tests here.
import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)  # Replace with your SMTP server and port
    server.starttls()  # Use TLS encryption
    server.login('anupkumarmridha.tech@gmail.com', 'jonwihpdefhrcwsk')  # Replace with your email and password
    server.quit()
    print("SMTP connection successful.")
except Exception as e:
    print("SMTP connection error:", str(e))
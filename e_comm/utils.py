import pyotp
from datetime import datetime, timedelta
from django.conf import settings
from django.core.mail import send_mail


def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32(), interval=300) # 5 minute validity
    return totp.now()

def verification(otp, user_otp):
    return otp == user_otp



def send_email(email_otp,to_email):
    send_mail(
        "Quick Del OTP",
        f"Quick Del: Use OTP {email_otp} to log in to your account. DO NOT SHARE this code with anyone, including the delivery agents.",
        settings.EMAIL_HOST_USER,
        [to_email],
        fail_silently=False,
    )


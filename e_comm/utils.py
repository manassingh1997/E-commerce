import pyotp
from datetime import datetime, timedelta

def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32(), interval=300) # 5 minute validity
    return totp.now()

def verification(otp, user_otp):
    return otp == user_otp
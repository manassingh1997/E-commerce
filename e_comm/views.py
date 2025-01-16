from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .models import CustomUser
from .utils import generate_otp, verification
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')


        user = CustomUser.objects.filter(phone_number = phone_number)

        if user.exists():
            messages.warning(request,'User exists Please Login')
            return redirect('login_page')
        
        user = CustomUser.objects.create_user(username=phone_number,phone_number=phone_number)
        
        mobile_otp = generate_otp()
        user.mobile_otp = mobile_otp
        user.save()

        print(f"Mobile OTP {mobile_otp}")

        request.session['phone_number'] = phone_number
        print(phone_number)
        return redirect('verify_otp', user_id = user.id)
    
    return render(request,'register.html')


def verify_otp(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    phone_number = request.session.get('phone_number')
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp5 = request.POST.get('otp5')
        otp6 = request.POST.get('otp6')
        mobile_otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6
        
        if verification(mobile_otp, user.mobile_otp):
            user.is_mobile_verified = True
            user.mobile_otp = None
            user.save()
            login(request,user)
            return redirect('index')
        else:
            return render(request, 'verify_otp.html', {'error':'Invalid OTP','phone_number':phone_number})
        
    return render(request, 'verify_otp.html')

def index(request):
    return render(request,'index.html')


def login_page(request):
    return render(request,'login.html')

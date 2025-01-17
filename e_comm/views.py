from django.shortcuts import render, redirect
from django.contrib.auth import login 
from .models import CustomUser
from .utils import *
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')


        user = CustomUser.objects.filter(email = email)

        if user.exists():
            messages.warning(request,'User exists Please Login')
            return redirect('login_page')
        
        user = CustomUser.objects.create_user(username=email,email = email)
        
        mobile_otp = generate_otp()
        user.mobile_otp = mobile_otp
        email_otp = generate_otp()
        user.email_otp = email_otp
        user.save()

        send_email(email_otp,email)
        #print(f"Mobile OTP {mobile_otp}")
        print(f"Email OTP {email_otp}")
        


        request.session['email'] = email
        return redirect('verify_otp', user_id = user.id)
    
    return render(request,'register.html')


def verify_otp(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    email = request.session.get('email')
    if request.method == 'POST':
        otp1 = request.POST.get('otp1')
        otp2 = request.POST.get('otp2')
        otp3 = request.POST.get('otp3')
        otp4 = request.POST.get('otp4')
        otp5 = request.POST.get('otp5')
        otp6 = request.POST.get('otp6')
        email_otp = otp1 + otp2 + otp3 + otp4 + otp5 + otp6
        
        if verification(email_otp, user.email_otp):
            user.is_email_verified = True
            user.email_otp = None
            user.save()
            login(request,user)
            return redirect('index')
        else:
            return render(request, 'verify_otp.html', {'error':'Invalid OTP','email':email})
        
    return render(request, 'verify_otp.html')

def index(request):
    return render(request,'index.html')


def login_page(request):
    return render(request,'login.html')

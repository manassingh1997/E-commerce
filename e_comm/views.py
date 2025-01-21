from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        user = CustomUser.objects.filter(email=email)

        #If user exists alreadey then throw a warning and return to same page
        if user.exists():
           messages.warning(request,"Account exists with Email")
           return redirect('/register/')

        if password != confirm_password:
            messages.warning(request,'Password and confirm password do not match')
            return redirect('/register/')
        
        try: 
           validate_password(password)
        except ValidationError as e:
            for error in e:
              messages.error(request,error)
            return redirect('/register/')
        

        user = CustomUser.objects.create(
           email = email,
           password = password,
           username = email,
        )

        user.set_password(password)
        user.save()
        user_instance = CustomUser.objects.first()
        user = authenticate(username = user_instance.username, password = password)

        if user:
           login(request,user)
           return redirect('index')

        return redirect('index')
    
    return render(request,'register.html')



def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = CustomUser.objects.filter(email = email)

        if not user.exists():
           messages.warning(request, "User Does Not Exists Please Sign Up")
           return redirect('login_page')
        
        user_instance = CustomUser.objects.first()
        user = authenticate(username = user_instance.username, password = password)
        if user:
           login(request,user)
           return redirect('index')
        
        messages.warning(request, 'Invalid Credentials')
        return redirect('login_page')
    
    return render(request,'login.html')
    
        

    

def logout_page(request):
    logout(request)
    return redirect('index')

def index(request):
    user = request.user

    return render(request,'index.html',{'user':user})
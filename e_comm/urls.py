from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login_page, name='login_page'),
    path('register/', register, name='register'),
    path('register-vo/<int:user_id>', verify_otp, name='verify_otp'),
]
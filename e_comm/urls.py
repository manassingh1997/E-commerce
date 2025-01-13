from django.contrib import admin
from django.urls import path
from .views import *

urlspattern = [
    path('', index, name='index.html'),
]
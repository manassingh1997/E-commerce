from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, unique=True)
    is_mobile_verified = models.BooleanField(default=False)
    is_email_verified = models.BooleanField(default=False)
    email_otp = models.CharField(max_length=6, null=True, blank=True)
    mobile_otp = models.CharField(max_length=6, null=True, blank=True)

    # Custom reverse relationships for groups and user_permissions
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Custom related_name to avoid conflicts
        blank=True
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',  # Custom related_name to avoid conflicts
        blank=True
    )

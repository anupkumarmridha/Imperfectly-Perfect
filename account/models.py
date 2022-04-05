from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    user_type_data = ((1, "Admin"),(2, "Customer"), (3, "Company"))
    # user_type = models.CharField(choices=user_type_data, max_length=20)
    user_type = models.CharField(default=2, choices=user_type_data, max_length=20)
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    gender_choice=(('M',"Male"),('F',"Female"))
    gender = models.CharField(choices=gender_choice, max_length=20)
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/customer/profile/')
    phone = models.CharField(max_length=13)
    dob = models.DateField()
    address = models.TextField()
    pin=models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)

class Company(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    
    company_name=models.CharField(max_length=50)
    cin=models.CharField(max_length=21)
    company_desc=models.TextField(null=True, blank=True)
    
    # gender_choice=(('M',"Male"),('F',"Female"))
    # gender = models.CharField(null=True, blank=True, choices=gender_choice, max_length=20)
    
    profile_pic = models.ImageField(null=True, blank=True,upload_to='images/company/profile/')
    
    phone = models.CharField(max_length=13)
    since = models.DateField()
    address = models.TextField()
    pin=models.CharField(max_length=6)
    
    website_url=models.CharField(max_length=255,null=True, blank=True)
    facebook_url=models.CharField(max_length=255,null=True, blank=True)
    twitter_url=models.CharField(max_length=255,null=True, blank=True)
    instagram_url=models.CharField(max_length=255,null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.user)


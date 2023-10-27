from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class CustomUser(AbstractUser):
    img = models.FileField(upload_to = 'images/',null = True,blank = True)
    text = models.CharField(max_length=50,validators=[validators.EmailValidator('test')])
    remember_me = models.BooleanField( null=True)





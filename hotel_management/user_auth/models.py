from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

USER_TYPE = (
    ('manager', 'Manager'),
    ('customer', 'Customer')
)

class User(AbstractUser):
    user_type = models.CharField(max_length=20,choices=USER_TYPE,default='customer')
    address = models.CharField(max_length=300,blank=True,null=True)
    phone = models.CharField(max_length=10,blank=True)
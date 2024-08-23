from django.db import models

# Create your models here.
from django.contrib.auth.models import User
  
  
class signup(models.Model):
    first_name = models.CharField(max_length=20,unique=True)
    last_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=50)
    phone_no = models.IntegerField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self):
        signup_page = f"{self.first_name}"
        return signup_page
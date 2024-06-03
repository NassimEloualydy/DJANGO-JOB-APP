from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    status=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    
    def __str__(self):
        return self.first_name+" "+self.last_name
# Create your models here.

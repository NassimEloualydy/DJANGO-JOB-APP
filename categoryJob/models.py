from django.db import models
from django.utils import timezone

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

def __str__(self):
    
    return self.name


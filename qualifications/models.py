from django.db import models
from django.utils import timezone
# Create your models here.
class Qualifications(models.Model):
    color=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    def __str__(self):
        return self.name 
        
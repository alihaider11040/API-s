from django.db import models

# Create your models here.
class employees(models.Model):
    fname=models.CharField(max_length=10)
    lname=models.CharField(max_length=10)
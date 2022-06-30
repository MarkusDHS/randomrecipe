from django.db import models
from django.db.models.fields import AutoField, BooleanField, TextField

# Create your models here.

class Receipt(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    picture=models.CharField(max_length=200)
    ingredients=models.TextField(max_length=2000)
    instructions=models.TextField(max_length=20000)

    
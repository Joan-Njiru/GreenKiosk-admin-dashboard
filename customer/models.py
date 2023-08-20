from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=32)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    location=models.CharField(max_length=30)
    identification=models.CharField(max_length=8)
    password=models.CharField(max_length=20)


    def __str__(self):
        return self.name

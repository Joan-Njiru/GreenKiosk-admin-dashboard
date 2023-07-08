from django.db import models

# Create your models here.
class Vendor(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField()
    phone_number=models.CharField(max_length=24)
    location=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    
    def __str__(self):
        return self.name


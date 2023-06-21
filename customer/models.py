from django.db import models

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=32)
    email=models.EmailField()
    phone_number=models.CharField(max_length=15)
    location=models.CharField(max_length=30)
    identification=models.CharField(max_length=8)
    password=models.CharField(max_length=20)
    payment=models.DecimalField(max_digits=20,decimal_places=3)

    def __str__(self):
        return self.email

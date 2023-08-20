from django.db import models
# from inventory.models import Product
# Create your models here.
class Vendor(models.Model):
    name = models.CharField (max_length=32)
    email = models.EmailField()
    phone_number = models.IntegerField ()
    location= models.CharField (max_length=32)
    password = models.PositiveBigIntegerField()
    # products = models.ManyToManyField(Product)

    def __str__(self):
        return self.name
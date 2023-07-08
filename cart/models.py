from django.db import models
from django.contrib.auth.models import User
from inventory.models import Product
from orders.models import Orders

# Create your models here.
class Cart(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=32)
    products = models.ManyToManyField(Product)
    number_of_items=models.IntegerField()
    payment=models.DecimalField(max_digits=20,decimal_places=2)
    

    def __str__(self):
        return self.products





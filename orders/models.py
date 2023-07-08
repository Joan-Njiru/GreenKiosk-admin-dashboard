from django.db import models
# from inventory.models import Product
from payment.models import Payment
from customer.models import Customer
# from cart.models import Cart


# Create your models here.
class Orders(models.Model):
    # products=models.ManyToManyField(Product)
    customer = models.ManyToManyField(Customer)
    payment = models.ManyToManyField(Payment)
    # customer_order = models.ForeignKey(Cart,on_delete=models.CASCADE)
    
    placement_date_time=models.DateTimeField()
    order_status=models.CharField(max_length=24)
    no_of_orders=models.IntegerField()
    total_order=models.IntegerField()
    
    def __str__(self):
        return self.order_status

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


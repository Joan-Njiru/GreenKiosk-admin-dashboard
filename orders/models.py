from django.db import models
from payment.models import Payment
from customer.models import Customer


# Create your models here.
class Orders(models.Model):
    customer = models.ManyToManyField(Customer)
    payment = models.ManyToManyField(Payment)
    placement_date_time=models.DateTimeField()
    order_status=models.CharField(max_length=24)
    no_of_orders=models.IntegerField()
    total_order=models.IntegerField()
    
    def __str__(self):
        return self.order_status

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"


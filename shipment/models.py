from django.db import models
from orders.models import Orders

# Create your models here.
class Shipment(models.Model):
    customer_order = models.ManyToManyField(Orders)
    date_of_shipment_placement=models.DateTimeField(auto_now_add=True)
    mode_of_delivery=models.CharField(max_length=48)
    location=models.CharField(max_length=32)
    phone_number=models.IntegerField()
    
    def __str__(self):
        return self.mode_of_delivery

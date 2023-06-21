from django.db import models

# Create your models here.
class Orders(models.Model):
    order_id=models.CharField(max_length=32)
    placement_date_time=models.DateTimeField()
    order_status=models.CharField(max_length=32)
    no_of_orders=models.IntegerField()
    total_order=models.IntegerField()
    
    def __str__(self):
        return self.order_id


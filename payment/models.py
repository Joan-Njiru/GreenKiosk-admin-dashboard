from django.db import models

# Create your models here.
class Payment(models.Model):
    amount=models.IntegerField()
    payment_date_time=models.DateTimeField()
    payment_status=models.BooleanField()
    receipt=models.CharField(max_length=48)
    payment_method=models.CharField(max_length=32)
    
    def __str__(self):
        return self.receipt


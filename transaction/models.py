from django.db import models

# Create your models here.
class Transaction(models.Model):
    transaction_note=models.TextField()
    transaction_id=models.IntegerField()
    order=models.CharField(max_length=24)
    products=models.CharField(max_length=32)
    def __str__(self):
        return self.transaction_id

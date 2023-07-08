from django.db import models

# Create your models here.
class Transaction(models.Model):
    transaction_note=models.CharField(max_length=48)
    transaction_id=models.IntegerField()

    def __str__(self):
        return self.transaction_note

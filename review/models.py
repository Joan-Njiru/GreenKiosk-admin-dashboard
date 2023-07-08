from django.db import models

# Create your models here.
class Review(models.Model):
    message=models.CharField(max_length=48)
    time_and_date=models.DateTimeField()
    sender_name=models.CharField(max_length=24)
    
    def __str__(self):
        return self.message


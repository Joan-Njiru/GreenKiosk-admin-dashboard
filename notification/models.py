from django.db import models

# Create your models here.
class Notification(models.Model):
    sender_name=models.CharField(max_length=32)
    title=models.CharField(max_length=24)
    description=models.CharField(max_length=42)
    message=models.TextField(max_length=48)
    date_and_time=models.DateTimeField()
    
    def __str__(self):
        return self.title

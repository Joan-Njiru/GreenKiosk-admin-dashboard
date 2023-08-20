from django.db import models

# from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):

    name = models.CharField(max_length=32)
    description = models.TextField()
    image = models.ImageField(upload_to="media")
    price = models.DecimalField(max_digits=6,decimal_places=2)
    stock = models.PositiveIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
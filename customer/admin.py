from django.contrib import admin

# Register your models here.
from.models import Customer
class CustomerAdmin(admin.ModelAdmin):
    customer = ('name','email','phone_number','location','identification','payment','password')
    admin.site.register(Customer)
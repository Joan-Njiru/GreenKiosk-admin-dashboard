from django.contrib import admin

# Register your models here.
from.models import Customer
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone_number','location','identification','password')
    
admin.site.register(Customer,CustomerAdmin)
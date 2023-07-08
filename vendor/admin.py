from django.contrib import admin

# Register your models here.
from.models import Vendor
class VendorAdmin(admin.ModelAdmin):
    list_display = ('name','phone_number','email','location','password')
    admin.site.register(Vendor)

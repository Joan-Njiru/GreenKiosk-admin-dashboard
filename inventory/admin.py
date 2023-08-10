from django.contrib import admin
from .models import Product

#creating an admin dashboard
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","description","image","stock","price","date_created","date_updated")
    
admin.site.register(Product,ProductAdmin)

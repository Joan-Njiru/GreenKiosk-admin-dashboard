from django.contrib import admin
from .models import Product

#creating an admin dashboard
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","stock","price","date_created")
admin.site.register(Product,ProductAdmin)

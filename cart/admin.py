from django.contrib import admin

# Register your models here.
from.models import Cart
class CartAdmin(admin.ModelAdmin):
    list_display = ('category','number_of_items','payment')

admin.site.register(Cart,CartAdmin)


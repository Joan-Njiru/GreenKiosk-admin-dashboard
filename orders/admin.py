from django.contrib import admin

# Register your models here.
from.models import Orders
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('placement_date_time','order_status','no_of_orders','total_order')

admin.site.register(Orders,OrdersAdmin)


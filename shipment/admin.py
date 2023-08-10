from django.contrib import admin

# Register your models here.
from.models import Shipment
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('date_of_shipment_placement','mode_of_delivery','location')

admin.site.register(Shipment,ShipmentAdmin)


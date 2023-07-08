from django.contrib import admin

# Register your models here.
from.models import Payment
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount','payment_date_time','payment_status','receipt','payment_method')

admin.site.register(Payment,PaymentAdmin)

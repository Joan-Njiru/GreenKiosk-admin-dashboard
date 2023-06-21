from django.contrib import admin

# Register your models here.
from.models import Payment
class TransactionAdmin(admin.ModelAdmin):
    orders = ('amount','payment_date_time','payment_status','receipt','payment_method')
    admin.site.register(Payment)

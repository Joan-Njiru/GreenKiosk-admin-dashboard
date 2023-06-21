from django.contrib import admin

# Register your models here.
from.models import Transaction
class TransactionAdmin(admin.ModelAdmin):
    transaction = ('transaction_note','transaction_id','order','products')
    admin.site.register(Transaction)
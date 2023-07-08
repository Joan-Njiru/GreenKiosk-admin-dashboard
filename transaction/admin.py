from django.contrib import admin

# Register your models here.
from.models import Transaction
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_note','transaction_id')

admin.site.register(Transaction,TransactionAdmin)
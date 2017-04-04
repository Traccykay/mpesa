from django.contrib import admin
from mpesa.models import Transaction

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('phone_number', 'amount', 'date_of_transaction', 'cost', 'transaction_type',)

admin.site.register(Transaction, TransactionAdmin)
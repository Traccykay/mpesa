from django.contrib import admin
from mpesa.models import Transaction
from mpesa.models import CustomerDetails

# Register your models here.

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('phone_number', 'amount', 'date_of_transaction', 'cost', 'transaction_type',)

class CustomerAdmin(admin.ModelAdmin):
	list_display = ('customer','Identification', 'mpesa_code', 'date_of_transaction', 'amount', 'signature',)

admin.site.register(Transaction, TransactionAdmin)
admin.site.register(CustomerDetails, CustomerAdmin)
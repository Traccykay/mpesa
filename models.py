from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Transaction(models.Model):
	DEPOSIT = 'DP'
	WITHDRAW = 'WD'
	NATIONALID = 'ID'
	Type_of_transactions = (
 		(DEPOSIT, 'Deposit'),
 		(WITHDRAW, 'Withdraw'),
 		)

	amount = models.PositiveSmallIntegerField()
	date_of_transaction = models.DateTimeField()
	transaction_type = models.CharField(max_length=20, choices=Type_of_transactions, default=DEPOSIT,)
	cost = models.IntegerField()
	phone_number = PhoneNumberField(unique=True)
	agent_name = models.CharField(max_length=50)

	# def get_transaction():
	# 	return Transaction.objects.get(id=1)


class CustomerDetails(models.Model):
	customer = models.ForeignKey(Transaction, null=True)
	Identification = models.PositiveSmallIntegerField()
	mpesa_code = models.CharField(max_length=20, unique=True,)
	date_of_transaction = models.DateTimeField()
	amount = models.IntegerField()
	signature =models.CharField(max_length=50)
	# customer = models.ForeignKey(Transaction, on_delete=models.CASCADE, default=3,)
	# customer = models.OneToOneField(Transaction, on_delete=models.CASCADE, default=3,)
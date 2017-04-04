from django.db import models

# Create your models here.
class Transaction(models.Model):
	DEPOSIT = 'DP'
	WITHDRAW = 'WD'
	Type_of_transactions = (
 		(DEPOSIT, 'Deposit'),
 		(WITHDRAW, 'Withdraw'),
 		)


	amount = models.PositiveSmallIntegerField()
	date_of_transaction = models.DateTimeField()
	transaction_type = models.CharField(max_length=20, choices=Type_of_transactions, default=DEPOSIT,)
	cost = models.IntegerField()
	phone_number = models.CharField(max_length=20)


class CustomerDetails(models.Model):
	national_id = models.IntegerField()
	mpesa_code = models.CharField(max_length=20)
	date_of_transaction = models.DateTimeField()
	amount = models.IntegerField()
	signature =models.CharField(max_length=50)
	# customer = models.ForeignKey(Transaction, on_delete=models.CASCADE, default=3,)
	customer = models.OneToOneField(Transaction, on_delete=models.CASCADE, default=3,)
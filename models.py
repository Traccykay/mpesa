from django.db import models

# Create your models here.
class Transaction(models.Model):
	DEPOSIT = 'DP'
	WITHDRAW = 'WD'
	Type_of_transactions = (
 		(DEPOSIT, 'Deposit'),
 		(WITHDRAW, 'Withdraw'),
 		)


	amount = models.IntegerField()
	date_of_transaction = models.DateTimeField()
	transaction_type = models.CharField(max_length=20, choices=Type_of_transactions, default=DEPOSIT,)
	cost = models.IntegerField()
	phone_number = models.CharField(max_length=20)

from django.db import models

# Create your models here.
class Transaction(models.Model):
	amount = models.IntegerField()
	date_of_transaction = models.DateTimeField()
	transaction_type = models.CharField(max_length=20)
	cost = models.IntegerField()
	phone_number = models.CharField(max_length=20)

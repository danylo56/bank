from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField()
    bill_number = models.CharField(max_length=10, unique=True)


class Transaction(models.Model):
    from_card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="transaction_from")
    to_card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="transaction_to")
    message = models.TextField()

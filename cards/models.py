from django.contrib.auth.models import User
from django.db import models


class Card(models.Model):
    holder = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    bill_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'№{self.bill_number} -> ${self.balance}'

    def visa_or_mastercard(self):
        return 'VISA' if int(self.bill_number[0]) % 2 == 0 else 'MasterCard'


class Transaction(models.Model):
    from_card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="transaction_from")
    to_card = models.ForeignKey(Card, on_delete=models.PROTECT, related_name="transaction_to")
    message = models.TextField()
    value = models.FloatField()

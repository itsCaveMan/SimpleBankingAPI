from django.db import models

from BankingAPI import globals
from BankingAPI.globals import BaseModel
from Users.models import User



class Account(BaseModel):

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='sender_user')

    account_type = models.CharField(max_length=255, choices=globals.ACCOUNT_TYPE_CHOICES, default=globals.UNDEFINED_ACCOUNT_TYPE)

    @property
    def balance(self):
        sum = 0
        # all_transactions = self.transaction.objects.all()
        all_transactions = Transaction.objects.filter(account=self)
        for t in all_transactions:
            if t.transaction_type == globals.DEPOSIT:
                sum += t.change_amount
            elif t.transaction_type == globals.WITHDRAWAL:
                sum -= t.change_amount
        return sum

    #MAYBE: amount = method to tally all deposit, expense to sum up amount

class Transaction(BaseModel):

    account = models.ForeignKey(Account, on_delete=models.PROTECT)

    change_amount = models.DecimalField(max_digits=12, decimal_places=8)

    transaction_type = models.CharField(max_length=255, choices=globals.TRANSACTION_TYPES_CHOICES, default=globals.UNDEFINED_TRANSACTION_TYPE)

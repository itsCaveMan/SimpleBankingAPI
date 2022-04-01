from django.db import models


# ==============   Models   ==============
class BaseModel(models.Model):
    created_on_utc = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified_utc = models.DateTimeField(auto_now=True,)

    class Meta:
        abstract = True

SAVINGS_ACCOUNT = 'SAVINGS_ACCOUNT'
CREDIT_ACCOUNT = 'CREDIT_ACCOUNT'
UNDEFINED_ACCOUNT_TYPE = 'UNDEFINED_ACCOUNT_TYPE'
ACCOUNT_TYPE_CHOICES = (
    (SAVINGS_ACCOUNT , 'Savings Account'),
    (CREDIT_ACCOUNT , 'Credit Account'),
    (UNDEFINED_ACCOUNT_TYPE , 'Undefined Account type'),
)

DEPOSIT = 'DEPOSIT'
WITHDRAWAL = 'WITHDRAWAL'
UNDEFINED_TRANSACTION_TYPE = 'UNDEFINED_TRANSACTION_TYPE'
TRANSACTION_TYPES_CHOICES = (
    (DEPOSIT , 'Deposit'),
    (WITHDRAWAL , 'Withdrawal'),
    (UNDEFINED_TRANSACTION_TYPE , 'Undefined Transaction type'),
)

"""Credit model."""

# Django
from django.db import models

# Models
from accounts.models.base import BaseModel
from accounts.models.accounts import Account


class Credit(BaseModel):
    account = models.ForeignKey(Account, related_name="credit_operations", on_delete=models.CASCADE)
    amount = models.DecimalField(decimal_places=2, max_digits=15)

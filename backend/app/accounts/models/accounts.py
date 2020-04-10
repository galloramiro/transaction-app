"""Account model."""

# Django
from django.db import models

# Models
from accounts.models.base import BaseModel


class Account(BaseModel):
    name = models.CharField(max_length=60)
    balance = models.DecimalField(decimal_places=2, max_digits=15)

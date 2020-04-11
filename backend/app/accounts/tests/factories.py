"""Meet up factory"""
# Factory
import factory

# Models
from accounts.models import Account, Credit, Debit

# Utils
import datetime
from decimal import Decimal




class AccountFactory(factory.DjangoModelFactory):
    class Meta:
        model = Account
    
    balance = Decimal("10000") 


class CreditFactory(factory.DjangoModelFactory):
    class Meta:
        model = Credit

    amount = Decimal("15")

class DebitFactory(factory.DjangoModelFactory):
    class Meta:
        model = Debit

    account = factory.SubFactory(AccountFactory)
    amount = Decimal("-10")

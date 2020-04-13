"""Account serializers"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Account

# Serializers
from accounts.serializers.credits import CreditModelSerializer
from accounts.serializers.debits import DebitModelSerializer


class AccountModelSerializer(serializers.ModelSerializer):

    credit_operations = CreditModelSerializer(read_only=True, many=True)
    debit_operations = DebitModelSerializer(read_only=True, many=True)
    transactions = serializers.SerializerMethodField()

    class Meta:
        """Meta class."""

        model = Account
        fields = (
            "balance",
            "credit_operations",
            "debit_operations",
            "transactions",
        )

    def get_transactions(self, account: Account):
        credit_op = CreditModelSerializer(account.credit_operations, read_only=True, many=True).data
        debits_op = DebitModelSerializer(account.debit_operations, read_only=True, many=True).data
        return credit_op + debits_op
        

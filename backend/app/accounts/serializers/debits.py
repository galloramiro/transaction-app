"""Debits serializer"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Debit


class DebitModelSerializer(serializers.ModelSerializer):

    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        """Meta class."""

        model = Debit
        fields = (
            "amount",
            "date",
            "time",        
        )
    
    def get_date(self, debit: Debit):
        return debit.created.date().strftime("%d/%m/%Y")
    
    def get_time(self, debit: Debit):
        return debit.created.time().strftime("%H:%M")


class CreateDebitSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class."""

        model = Debit
        fields = ("amount",)

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError(
            "You are traing to make a negative debit operation"
        )

        account_balance = self.initial_data["account"].balance
        if account_balance - amount < 0:
            raise serializers.ValidationError(
            "You don't have enough money in the account to perform this operation"
        )

        return amount
    
    def create(self, data):
        account = self.initial_data["account"] 
        amount = data["amount"]
        debit = Debit.objects.create(account=account, amount=amount)
        account.balance -= amount
        account.save()
        return debit

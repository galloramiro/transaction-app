"""Credit serializer"""

# Django REST Framework
from rest_framework import serializers

# Models
from accounts.models import Credit


class CreditModelSerializer(serializers.ModelSerializer):

    date = serializers.SerializerMethodField()
    time = serializers.SerializerMethodField()

    class Meta:
        """Meta class."""

        model = Credit
        fields = (
            "amount",
            "date",
            "time",        
        )
    
    def get_date(self, credit: Credit):
        return credit.created.date().strftime("%d/%m/%Y")
    
    def get_time(self, credit: Credit):
        return credit.created.time().strftime("%H:%M")


class CreateCreditSerializer(serializers.ModelSerializer):

    class Meta:
        """Meta class."""

        model = Credit
        fields = ("amount",)

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError(
            "You are traing to make a negative credit operation"
        )
        return amount
    
    def create(self, data):
        account = self.initial_data["account"] 
        amount = data["amount"]
        credit = Credit.objects.create(account=account, amount=amount)
        account.balance += amount
        account.save()
        return credit

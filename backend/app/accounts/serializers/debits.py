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

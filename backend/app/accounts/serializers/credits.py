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

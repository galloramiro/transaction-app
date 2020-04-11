"""Account views."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from accounts.models import Account

# Serializers
from accounts.serializers import AccountModelSerializer


class AccountViewSet(viewsets.GenericViewSet):
    """Account view set.
    
    Handle the creation of deposits, credits and 
    retrive the balance of the account. 
    """

    queryset = Account.objects.all()
    
    def get_serializer_class(self):
        if self.action == "balance":
            return AccountModelSerializer
    
    @action(detail=True, methods=['get'])
    def balance(self, request, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(self.get_object()).data
        return Response(serializer)

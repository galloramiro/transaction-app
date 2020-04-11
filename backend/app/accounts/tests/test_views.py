"""Test account views."""
# Built in
from datetime import datetime, timezone, timedelta
from urllib.parse import urlencode

# Pytest
import pytest

# Django
from django.urls import reverse

# Django REST Framework
from rest_framework import status
from rest_framework.test import APIClient

# Factories
from accounts.tests.factories import (
    AccountFactory,
    CreditFactory,
    DebitFactory,
)


@pytest.mark.django_db
def test_account_view_set():
    client = APIClient()
    account = AccountFactory()
    CreditFactory(account=account)
    CreditFactory(account=account)
    DebitFactory(account=account)
    
    CreditFactory
    DebitFactory()
    
    response = client.get(
        reverse("accounts:account-balance", args=(account.pk,)) 
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["balance"] == "10000.00"
    assert len(response.json()["credit_operations"]) == 2
    assert len(response.json()["debit_operations"]) == 1


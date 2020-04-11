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
def test_balance_account_view_set():
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


@pytest.mark.django_db
def test_create_credit_action():
    client = APIClient()
    account = AccountFactory()
    CreditFactory(account=account)
    DebitFactory(account=account)
        
    response = client.post(
        reverse("accounts:account-credit", args=(account.pk,)),
        dict(amount="1000")
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["balance"] == "11000.00"
    assert len(response.json()["credit_operations"]) == 2


@pytest.mark.django_db
def test_create_credit_action_with_negative_values():
    client = APIClient()
    account = AccountFactory()
    CreditFactory(account=account)
    DebitFactory(account=account)
        
    response = client.post(
        reverse("accounts:account-credit", args=(account.pk,)),
        dict(amount="-1000")
    )

    expected_response = dict(amount=["You are traing to make a negative credit operation"])

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response


@pytest.mark.django_db
def test_create_debit_action():
    client = APIClient()
    account = AccountFactory()
    CreditFactory(account=account)
    DebitFactory(account=account)
        
    response = client.post(
        reverse("accounts:account-debit", args=(account.pk,)),
        dict(amount="1000")
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["balance"] == "9000.00"
    assert len(response.json()["debit_operations"]) == 2


@pytest.mark.django_db
def test_create_debit_action_with_amount_greater_than_account_balance():
    client = APIClient()
    account = AccountFactory()
    CreditFactory(account=account)
    DebitFactory(account=account)
        
    response = client.post(
        reverse("accounts:account-debit", args=(account.pk,)),
        dict(amount="100000")
    )

    expected_response = dict(
        amount=["You don't have enough money in the account to perform this operation"]
    )

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert response.json() == expected_response

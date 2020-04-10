"""Circles admin."""

# Django
from django.contrib import admin

# Models
from accounts.models import (
    Account,
    Credit,
    Debit,
)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    """Account admin"""

    list_display = (
        'name',
        'balance',
        'created',
        'modified',
    )
    search_fields = ('name', 'modified')
    list_filter = (
        'created',
        'modified',
    )


@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    """Credit admin"""

    list_display = (
        'amount',
        'created',
        'modified',
    )
    search_fields = ('amount', 'created')
    list_filter = (
        'created',
        'modified',
    )


@admin.register(Debit)
class DebitAdmin(admin.ModelAdmin):
    """Debit admin"""

    list_display = (
        'amount',
        'created',
        'modified',
    )
    search_fields = ('amount', 'created')
    list_filter = (
        'created',
        'modified',
    )

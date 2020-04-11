"""Accoun URLs."""

# Django
from django.urls import path, include

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from accounts.views import AccountViewSet


router = DefaultRouter()
router.register(r"account", AccountViewSet, basename="account")

urlpatterns = [
    path("", include(router.urls)),
]

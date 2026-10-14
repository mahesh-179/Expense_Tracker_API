from rest_framework.routers import DefaultRouter
from .viewsets import UserViewSet, ProfileViewSet, TransactionViewSet
from django.urls import path, include
router = DefaultRouter()
router.register('users', UserViewSet)
router.register('profiles', ProfileViewSet)
router.register('transactions', TransactionViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
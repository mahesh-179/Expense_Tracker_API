from .serializers import UserSerializer, ProfileSerializer, TransactionSerializer
from .models import Profile, Transaction
from django.contrib.auth.models import User
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework.permissions import AllowAny
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes=[AllowAny]
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes=[IsOwnerOrReadOnly]
class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes=[IsOwnerOrReadOnly]

    
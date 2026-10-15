from django.db import models
from django.contrib.auth.models import User
class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=45, unique=True)
    address = models.CharField(max_length=30, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        INCOME = 'INCOME', 'Income'
        EXPENSE = 'EXPENSE', 'Expense'
    user = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TransactionType.choices)
    remarks = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.username}'s Transaction - {self.amount} on {self.date}"


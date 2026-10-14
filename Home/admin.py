from django.contrib import admin
from .models import Profile, Transaction
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'email', 'address', 'phone_number', 'joined_date')
    search_fields = ('user__username', 'full_name', 'email')
    list_filter = ('joined_date',)
admin.site.register(Profile, ProfileAdmin)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'remarks', 'date')
    search_fields = ('user__username', 'amount', 'type', 'remarks')
    list_filter = ('type', 'date')
admin.site.register(Transaction, TransactionAdmin)
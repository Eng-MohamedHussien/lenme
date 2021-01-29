from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'amount', 'due_date', 'loan', 'discharged')
    list_filter = ('due_date', 'discharged')

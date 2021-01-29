from django.contrib import admin
from .models import RequestedLoan, AcceptedLoan, Offer


@admin.register(RequestedLoan)
class RequestedLoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'loan_amount', 'loan_period', 'lenme_fee', 'created_at', 'status', 'borrower')
    list_filter = ('status', 'created_at', 'loan_period', 'borrower')


@admin.register(AcceptedLoan)
class AcceptedLoanAdmin(admin.ModelAdmin):
    list_display = ('id', 'requested_loan', 'accepted_offer', 'confirmed_at')
    list_filter = ('confirmed_at',)


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'investor', 'annual_interest_rate', 'created_at', 'loan')
    list_filter = ('investor', 'created_at')
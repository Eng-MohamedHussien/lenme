from rest_framework import serializers
from .models import RequestedLoan, Offer, AcceptedLoan


class RequestedLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestedLoan
        fields = ['id', 'loan_amount', 'loan_period', 'lenme_fee', 'created_at', 'status', 'borrower']
        read_only_fields = ('id', 'lenme_fee', 'created_at', 'status', 'borrower')


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = ['id', 'investor', 'annual_interest_rate', 'created_at', 'loan']
        read_only_fields = ('id', 'created_at', 'investor')


class AcceptedLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedLoan
        fields = ['id', 'requested_loan', 'accepted_offer']
        read_only_fields = ('id',)
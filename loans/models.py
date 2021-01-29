from django.db import models
from users.models import CustomUser


class RequestedLoan(models.Model):
    loan_amount = models.FloatField()
    loan_period = models.IntegerField()
    lenme_fee = models.FloatField(default=3.0)
    created_at = models.DateField(auto_now_add=True)
    states = [(status, status) for status in ['Requested', 'Funded', 'Completed']]
    status = models.CharField(choices=states, max_length=9, default='Requested')
    borrower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='loans')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Loan amount {self.loan_amount} for {self.loan_period} requested at {self.created_at} to {self.borrower}"

    def total_loan_amount(self):
        return self.loan_amount + self.lenme_fee

    def num_years(self):
        return self.loan_period / 12


class Offer(models.Model):
    investor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='investments')
    annual_interest_rate = models.FloatField()
    created_at = models.DateField(auto_now_add=True)
    loan = models.ForeignKey(RequestedLoan, on_delete=models.CASCADE, related_name='offers')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Offer annual interest rate {self.annual_interest_rate} by {self.investor} at {self.created_at}"


class AcceptedLoan(models.Model):
    confirmed_at = models.DateField(auto_now_add=True)
    requested_loan = models.OneToOneField(RequestedLoan, on_delete=models.CASCADE, related_name='accepted_loan')
    accepted_offer = models.OneToOneField(Offer, on_delete=models.CASCADE, related_name='accepted_loan')

    class Meta:
        ordering = ['confirmed_at']

    def __str__(self):
        return f"loan get accepted at {self.confirmed_at}"


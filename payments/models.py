from django.db import models
from loans.models import RequestedLoan


class Payment(models.Model):
    amount = models.FloatField()
    due_date = models.DateField()
    loan = models.ForeignKey(RequestedLoan, on_delete=models.CASCADE, related_name='payments')
    discharged = models.BooleanField(default=False)

    def __str__(self):
        return f'Payment amount is {self.amount} in {self.due_date}'

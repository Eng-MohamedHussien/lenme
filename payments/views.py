from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Payment
from datetime import date
from django.http import Http404
from .serializers import PaymentSerializer


class TodayPaymentsView(APIView):
    def get(self, request):
        today_payments = Payment.objects.filter(due_date=date.today())
        serializer = PaymentSerializer(today_payments, many=True)
        return Response(serializer.data)
        

class DischargeView(APIView):
    def get(self, request, pk):
        try:
            payment = Payment.objects.get(pk=pk)
        except(Payment.DoesNotExist):
            raise Http404
        
        if payment.discharged:
            return Response({'process': 'has been done before'})
            
        payment.loan.borrower.balance -= payment.amount
        payment.loan.borrower.save()

        payment.loan.accepted_loan.accepted_offer.investor.balance += payment.amount
        payment.loan.accepted_loan.accepted_offer.investor.save()

        payment.discharged = True
        payment.save()

        if len(payment.loan.payments.filter(discharged=False)) == 0:
            payment.loan.status = 'Completed'
            payment.loan.save()

        return Response({'process': 'completed successfully'})



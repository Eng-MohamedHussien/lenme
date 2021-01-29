from .serializers import RequestedLoanSerializer, OfferSerializer, AcceptedLoanSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import RequestedLoan
from payments.models import Payment
from dateutil.relativedelta import relativedelta
from django.http import Http404


class RequestedLoanCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        serializer = RequestedLoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(borrower=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OfferCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        serializer = OfferSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(investor=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AcceptedLoanCreateView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    
    def post(self, request):
        serializer = AcceptedLoanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FundLoanView(APIView):
    def get(self, request, pk):
        try:
            loan = RequestedLoan.objects.get(pk=pk)
        except(Loan.DoesNotExist):
            raise Http404
        
        if loan.status == 'Funded':
            return Response({'fund': 'has been done before'})

        loan.status = 'Funded'
        loan.save()

        loan.borrower.balance = loan.borrower.balance + loan.loan_amount
        loan.borrower.save()

        loan.accepted_loan.accepted_offer.investor.balance = loan.accepted_loan.accepted_offer.investor.balance - loan.total_loan_amount()
        loan.accepted_loan.accepted_offer.investor.save()

        total_loan = loan.loan_amount + ((loan.num_years()) * ((loan.loan_amount) * ((loan.accepted_loan.accepted_offer.annual_interest_rate) / 100)))
        loan_payment_per_month = total_loan / loan.loan_period
        date = loan.accepted_loan.confirmed_at
        
        for i in range(loan.loan_period):
            date += relativedelta(months=1)
            Payment.objects.create(amount=loan_payment_per_month, due_date=date, loan=loan)

        return Response({'fund': 'done'})
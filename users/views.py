from .models import CustomUser
from loans.models import Offer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


class CheckBalanceView(APIView):
    def get(self, request, investor_id, offer_id):
        try:
            investor = CustomUser.objects.get(id=investor_id)
        except(CustomUser.DoesNotExist):
            raise Http404
        try:
            offer = Offer.objects.get(id=offer_id)
        except(Offer.DoesNotExist):
            raise Http404
        
        balance = investor.balance
        loan_amount = offer.loan.total_loan_amount()

        if balance >= loan_amount:
            return Response({'invest_ability': True})
        else:
            return Response({'invest_ability': False})
from django.test import TestCase
from users.models import CustomUser
from rest_framework.test import APIRequestFactory, force_authenticate
from loans.views import RequestedLoanCreateView, OfferCreateView
from rest_framework.authtoken.models import Token
from loans.models import RequestedLoan


def create_user(username, email, password, balance):
    return CustomUser.objects.create(username=username, email=email, password=password, balance=balance)


# Create your tests here.
class LoanTests(TestCase):
    def test_request_loan(self):
        factory = APIRequestFactory()
        client = create_user('ahmed', 'ahmed_10@gmail.com', '1250$adfsdA', 1000.0)
        view = RequestedLoanCreateView.as_view()
        request = factory.post('/loans/create/', {'loan_amount': 2000.0, 'loan_period': 6}, format='json')
        force_authenticate(request, user=client, token=Token.objects.get(user=client))
        response = view(request)
        self.assertEqual(response.status_code, 201)
    
    def test_create_offer(self):
        factory = APIRequestFactory()
        borrower = create_user('ahmed', 'ahmed_10@gmail.com', '1250$adfsdA', 1000.0)
        investor = create_user('ali', 'ali_mo@gmail.com', '5000$rgrgrW', 10000.0)
        loan = RequestedLoan.objects.create(loan_amount=2000.0, loan_period=8, borrower=borrower)
        view = OfferCreateView.as_view()
        request = factory.post('/loans/offers/create/', {'annual_interest_rate': 5.6, 'loan': loan.pk}, format='json')
        force_authenticate(request, user=investor, token=Token.objects.get(user=investor))
        response = view(request)
        self.assertEqual(response.status_code, 201)




    
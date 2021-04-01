from django.test import TestCase
from users.models import CustomUser
from rest_framework.test import APIRequestFactory, force_authenticate
from users.views import CheckBalanceView
from rest_framework.authtoken.models import Token
from loans.models import RequestedLoan, Offer
from rest_framework.reverse import reverse


def create_user(username, email, password, balance):
    return CustomUser.objects.create(username=username, email=email, password=password, balance=balance)


# Create your tests here.
class UserTests(TestCase):    
    def test_investor_balance_1(self):
        factory = APIRequestFactory()
        borrower = create_user('ahmed', 'ahmed_10@gmail.com', '1250$adfsdA', 1000.0)
        investor = create_user('ali', 'ali_mo@gmail.com', '5000$rgrgrW', 10000.0)
        loan = RequestedLoan.objects.create(loan_amount=2000.0, loan_period=8, borrower=borrower)
        offer = Offer.objects.create(investor=investor, annual_interest_rate=5.6, loan=loan)
        view = CheckBalanceView.as_view()
        kwargs = {'investor_id': investor.pk, 'offer_id': offer.pk}
        request = factory.get(reverse('check_balance', kwargs=kwargs))
        response = view(request, **kwargs)
        self.assertEqual(response.data['invest_ability'], True)

    def test_investor_balance_2(self):
        factory = APIRequestFactory()
        borrower = create_user('ahmed', 'ahmed_10@gmail.com', '1250$adfsdA', 1000.0)
        investor = create_user('ali', 'ali_mo@gmail.com', '5000$rgrgrW', 2000.0)
        loan = RequestedLoan.objects.create(loan_amount=2000.0, loan_period=8, borrower=borrower)
        offer = Offer.objects.create(investor=investor, annual_interest_rate=5.6, loan=loan)
        view = CheckBalanceView.as_view()
        kwargs = {'investor_id': investor.pk, 'offer_id': offer.pk}
        request = factory.get(reverse('check_balance', kwargs=kwargs))
        response = view(request, **kwargs)
        self.assertEqual(response.data['invest_ability'], False)




    
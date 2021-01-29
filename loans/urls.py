from django.urls import path
from loans.views import RequestedLoanCreateView, OfferCreateView, AcceptedLoanCreateView, FundLoanView


urlpatterns = [
    path('create/', RequestedLoanCreateView.as_view()),
    path('offers/create/', OfferCreateView.as_view()),
    path('offers/accept/', AcceptedLoanCreateView.as_view()),
    path('fund/<int:pk>/', FundLoanView.as_view())   
]
from django.urls import path
from users.views import CheckBalanceView

urlpatterns=[
    path('check/balance/<int:investor_id>/<int:offer_id>/', CheckBalanceView.as_view(), name='check_balance')
]
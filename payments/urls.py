from django.urls import path
from .views import TodayPaymentsView, DischargeView

urlpatterns = [
    path('today/', TodayPaymentsView.as_view()),
    path('discharge/<int:pk>/', DischargeView.as_view()),
]
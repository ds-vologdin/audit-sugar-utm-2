from django.urls import path

from utm_billing.views import PayStatisticView

urlpatterns = [
    path('pay/', PayStatisticView.as_view(), name='pay'),
    path('pay/<int:year>/', PayStatisticView.as_view(), name='pay_year'),
    path('pay/<int:year>/<int:month>/', PayStatisticView.as_view(), name='pay_month'),
    path('pay/last/<str:last>/', PayStatisticView.as_view(), name='pay_last'),
]
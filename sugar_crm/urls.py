from django.urls import path

from .views import HardwareToRemoveView, OpenedTicketsView

urlpatterns = [
    path('hardware/', HardwareToRemoveView.as_view(), name='hardware_to_remove'),
    path('hardware/<int:year>/<int:month>/',
         HardwareToRemoveView.as_view(),
         name='hardware_to_remove_month'),
    path('tickets/', OpenedTicketsView.as_view(), name='opened_tickets'),
    path('tickets/<int:year>/', OpenedTicketsView.as_view(), name='opened_tickets'),
    path('tickets/last/<str:last>/', OpenedTicketsView.as_view(), name='opened_tickets'),
]
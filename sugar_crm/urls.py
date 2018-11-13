from django.urls import path

from .views import HardwareToRemoveView, OpenedTicketsView, TypeTicketsView

urlpatterns = [
    path('hardware/', HardwareToRemoveView.as_view(), name='hardware_to_remove'),
    path('hardware/<int:year>/<int:month>/',
         HardwareToRemoveView.as_view(),
         name='hardware_to_remove_month'),
    path('tickets/opened/', OpenedTicketsView.as_view(), name='opened_tickets'),
    path('tickets/opened/<int:year>/', OpenedTicketsView.as_view(), name='opened_tickets'),
    path('tickets/opened/last/<str:last>/', OpenedTicketsView.as_view(), name='last_opened_tickets'),
    path('tickets/types/', TypeTicketsView.as_view(), name='type_tickets'),
    path('tickets/types/<int:year>/', TypeTicketsView.as_view(), name='year_type_tickets'),
    path('tickets/types/<int:year>/<int:month>/', TypeTicketsView.as_view(), name='month_type_tickets'),
    path('tickets/types/last/<str:last>/', TypeTicketsView.as_view(), name='last_type_tickets'),
]
from django.urls import path

from .views import HardwareToRemoveView, OpenedTicketsView, TypeTicketsView
from .views import WrongedTicketsView

urlpatterns = [
    path('hardware/', HardwareToRemoveView.as_view(), name='hardware_to_remove'),
    path('hardware/<int:year>/<int:month>/',
         HardwareToRemoveView.as_view(),
         name='hardware_to_remove_month'),
    path('tickets/opened/', OpenedTicketsView.as_view(), name='opened_tickets'),
    path('tickets/opened/<int:year>/', OpenedTicketsView.as_view(), name='year_opened_tickets'),
    path('tickets/opened/<int:year>/<int:month>/', OpenedTicketsView.as_view(), name='month_opened_tickets'),
    path('tickets/opened/last/<str:last>/', OpenedTicketsView.as_view(), name='last_opened_tickets'),

    path('tickets/types/', TypeTicketsView.as_view(), name='type_tickets'),
    path('tickets/types/<int:year>/', TypeTicketsView.as_view(), name='year_type_tickets'),
    path('tickets/types/<int:year>/<int:month>/', TypeTicketsView.as_view(), name='month_type_tickets'),
    path('tickets/types/last/<str:last>/', TypeTicketsView.as_view(), name='last_type_tickets'),

    path('tickets/wronged/', WrongedTicketsView.as_view(), name='wronged_tickets'),
    path('tickets/wronged/<int:year>/', WrongedTicketsView.as_view(), name='year_wronged_tickets'),
    path('tickets/wronged/<int:year>/<int:month>/', WrongedTicketsView.as_view(), name='month_wronged_tickets'),
    path('tickets/wronged/last/<str:last>/', WrongedTicketsView.as_view(), name='last_wronged_tickets'),
]
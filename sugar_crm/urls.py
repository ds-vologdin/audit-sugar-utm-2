from django.urls import path, include

from .views import HardwareToRemoveView, OpenedTicketsView, TypeTicketsView
from .views import WrongedTicketsView, MassTicketsView, WrongedMassTicketsView
from .views import TopTicketsView, TopCallsView, TopNoServiceTicketsView

hardware_url_patterns = [
    path('', HardwareToRemoveView.as_view(), name='hardware_to_remove'),
    path('<int:year>/<int:month>/', HardwareToRemoveView.as_view(),
         name='hardware_to_remove_month'),
]

tickets_url_patterns = [
    path('opened/', OpenedTicketsView.as_view(), name='opened_tickets'),
    path('opened/<int:year>/', OpenedTicketsView.as_view(),
         name='year_opened_tickets'),
    path('opened/<int:year>/<int:month>/', OpenedTicketsView.as_view(),
         name='month_opened_tickets'),
    path('opened/last/<str:last>/', OpenedTicketsView.as_view(),
         name='last_opened_tickets'),

    path('types/', TypeTicketsView.as_view(), name='type_tickets'),
    path('types/<int:year>/', TypeTicketsView.as_view(),
         name='year_type_tickets'),
    path('types/<int:year>/<int:month>/', TypeTicketsView.as_view(),
         name='month_type_tickets'),
    path('types/last/<str:last>/', TypeTicketsView.as_view(),
         name='last_type_tickets'),

    path('wronged/', WrongedTicketsView.as_view(),
         name='wronged_tickets'),
    path('wronged/<int:year>/', WrongedTicketsView.as_view(),
         name='year_wronged_tickets'),
    path('wronged/<int:year>/<int:month>/', WrongedTicketsView.as_view(),
         name='month_wronged_tickets'),
    path('tickets/wronged/last/<str:last>/', WrongedTicketsView.as_view(),
         name='last_wronged_tickets'),

    path('mass/', MassTicketsView.as_view(), name='mass_tickets'),
    path('mass/<int:year>/', MassTicketsView.as_view(),
         name='year_mass_tickets'),
    path('mass/<int:year>/<int:month>/', MassTicketsView.as_view(),
         name='month_mass_tickets'),
    path('mass/last/<str:last>/', MassTicketsView.as_view(),
         name='last_mass_tickets'),

    path('wronged_mass/', WrongedMassTicketsView.as_view(), name='wronged_mass_tickets'),
    path('wronged_mass/<int:year>/', WrongedMassTicketsView.as_view(),
         name='year_wronged_mass_tickets'),
    path('wronged_mass/<int:year>/<int:month>/', WrongedMassTicketsView.as_view(),
         name='month_wronged_mass_tickets'),
    path('wronged_mass/last/<str:last>/', WrongedMassTicketsView.as_view(),
         name='last_wronged_mass_tickets'),

    path('top/', TopTicketsView.as_view(), name='top_tickets'),
    path('top/<int:year>/', TopTicketsView.as_view(), name='year_top_tickets'),
    path('top/<int:year>/<int:month>/', TopTicketsView.as_view(),
         name='month_top_tickets'),
    path('top/last/<str:last>/', TopTicketsView.as_view(),
         name='last_top_tickets'),

    path('calls/', TopCallsView.as_view(), name='top_calls'),
    path('calls/<int:year>/', TopCallsView.as_view(), name='year_top_calls'),
    path('calls/<int:year>/<int:month>/', TopCallsView.as_view(),
         name='month_top_calls'),
    path('calls/last/<str:last>/', TopCallsView.as_view(),
         name='last_top_calls'),

    path('no_service/', TopNoServiceTicketsView.as_view(), name='top_no_service'),
    path('no_service/<int:year>/', TopNoServiceTicketsView.as_view(),
         name='year_top_no_service'),
    path('no_service/<int:year>/<int:month>/', TopNoServiceTicketsView.as_view(),
         name='month_top_no_service'),
    path('no_service/last/<str:last>/', TopNoServiceTicketsView.as_view(),
         name='last_top_no_service'),
]

urlpatterns = [
    path('hardware/', include(hardware_url_patterns)),
    path('tickets/', include(tickets_url_patterns)),
]

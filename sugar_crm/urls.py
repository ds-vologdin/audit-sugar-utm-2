from django.urls import path, include

from .views import HardwareToRemoveView, OpenedTicketsView, TypeTicketsView
from .views import WrongedTicketsView, MassTicketsView

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
]

urlpatterns = [
    path('hardware/', include(hardware_url_patterns)),
    path('tickets/', include(tickets_url_patterns)),
]

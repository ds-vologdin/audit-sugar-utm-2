from django.urls import path

from .views import HardwareToRemove

urlpatterns = [
    path('hardware/', HardwareToRemove.as_view(), name='hardware_to_remove'),
    path(
        'hardware/<int:year>/<int:month>/',
        HardwareToRemove.as_view(),
        name='hardware_to_remove_month'
    ),
]
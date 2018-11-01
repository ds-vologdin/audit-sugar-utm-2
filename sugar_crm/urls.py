from django.urls import path

from .views import HardwareToRemoveView

urlpatterns = [
    path('hardware/', HardwareToRemoveView.as_view(), name='hardware_to_remove'),
    path(
        'hardware/<int:year>/<int:month>/',
        HardwareToRemoveView.as_view(),
        name='hardware_to_remove_month'
    ),
]
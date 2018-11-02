from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from utils.auth import access_group

from .sugar_utils.hardware_to_remove import fetch_hardware_to_remove


class HardwareToRemoveView(LoginRequiredMixin, View):
    template_name = "sugar_crm/hardware_to_remove.html"
    login_url = '/accounts/login/'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        hardware_to_remove = fetch_hardware_to_remove()

        context = {
            'hardware_to_remove': hardware_to_remove,
            'type_report': 'hardware_to_remove',
        }
        return render(request, self.template_name, context)

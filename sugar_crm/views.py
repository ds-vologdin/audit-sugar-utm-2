from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from utils.auth import access_group
from utils.helpers import get_report_begin_end_date
from utils.helpers import get_report_periods

from .sugar_utils.hardware_to_remove import fetch_hardware_to_remove
from .sugar_utils.tickets import get_statistic_of_opened_tickets
from .sugar_utils.tickets import get_statistic_of_type_tickets
from .sugar_utils.tickets import fetch_count_created_tickets_at_period


class HardwareToRemoveView(LoginRequiredMixin, View):
    template_name = 'sugar_crm/hardware_to_remove.html'
    login_url = reverse_lazy('login')

    @access_group('service')
    def get(self, request, *args, **kwargs):
        hardware_to_remove = fetch_hardware_to_remove()

        context = {
            'hardware_to_remove': hardware_to_remove,
            'type_report': 'hardware_to_remove',
        }
        return render(request, self.template_name, context)


class OpenedTicketsView(LoginRequiredMixin, View):
    template_name = 'sugar_crm/opened_tickets.html'
    login_url = reverse_lazy('login')

    @access_group('service')
    def get(self, request, *args, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        last = self.kwargs.get('last', 'quarter')

        date_begin, date_end = get_report_begin_end_date(year, month, last)

        statistic_of_opened_tickets = get_statistic_of_opened_tickets(
            date_begin, date_end)
        count_created_tickets = fetch_count_created_tickets_at_period(
            date_begin, date_end)

        context = {
            'statistic_of_opened_tickets': statistic_of_opened_tickets,
            'count_created_tickets': count_created_tickets,
            'type_report': 'tickets',
            'date_begin': date_begin,
            'date_end': date_end,
        }
        return render(request, self.template_name, context)


class TypeTicketsView(LoginRequiredMixin, View):
    template_name = 'sugar_crm/type_tickets.html'
    login_url = reverse_lazy('login')

    @access_group('service')
    def get(self, request, *args, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        last = self.kwargs.get('last', 'quarter')

        date_begin, date_end = get_report_begin_end_date(year, month, last)

        statistic_of_type_tickets = get_statistic_of_type_tickets(
            date_begin, date_end)

        context = {
            'statistic_of_type_tickets': statistic_of_type_tickets,
            'count_tickets': statistic_of_type_tickets.count_tickets,
            'count_not_correct_localisation':
                statistic_of_type_tickets.count_not_correct_localisation,
            'statistic_of_localisation':
                statistic_of_type_tickets.statistic_of_localisation,
            'type_report': 'tickets',
            'date_begin': date_begin,
            'date_end': date_end,
        }
        return render(request, self.template_name, context)
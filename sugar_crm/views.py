from django.views.generic import View
from django.shortcuts import render

from utils.auth import access_group
from django.contrib.auth.mixins import LoginRequiredMixin
from utils.mixins import GetPeriodMixin, DefaultContextMixin

from .sugar_utils.hardware_to_remove import fetch_hardware_to_remove
from .sugar_utils.tickets import get_statistic_of_opened_tickets
from .sugar_utils.tickets import get_statistic_of_type_tickets
from .sugar_utils.tickets import fetch_count_created_tickets_at_period
from .sugar_utils.tickets import fetch_wronged_tickets
from .sugar_utils.tickets import fetch_mass_tickets
from .sugar_utils.tickets import fetch_wronged_mass_tickets
from .sugar_utils.tickets import fetch_top_tickets
from .sugar_utils.tickets import fetch_top_calls_to_support


class HardwareToRemoveView(LoginRequiredMixin, View):
    template_name = 'sugar_crm/hardware_to_remove.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        hardware_to_remove = fetch_hardware_to_remove()

        context = {
            'hardware_to_remove': hardware_to_remove,
            'type_report': 'hardware_to_remove',
        }
        return render(request, self.template_name, context)


class DefaultTicketsViewMixin(DefaultContextMixin, GetPeriodMixin, LoginRequiredMixin):
    ...


class OpenedTicketsView(DefaultContextMixin, GetPeriodMixin, LoginRequiredMixin, View):
    template_name = 'sugar_crm/opened_tickets.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period('quarter')
        statistic_of_opened_tickets = get_statistic_of_opened_tickets(
            date_begin, date_end)
        count_created_tickets = fetch_count_created_tickets_at_period(
            date_begin, date_end)

        context = self.context.copy()
        context.update({
            'statistic_of_opened_tickets': statistic_of_opened_tickets,
            'count_created_tickets': count_created_tickets,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)


class TypeTicketsView(DefaultContextMixin, GetPeriodMixin, LoginRequiredMixin, View):
    template_name = 'sugar_crm/type_tickets.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period('quarter')
        statistic_of_type_tickets = get_statistic_of_type_tickets(
            date_begin, date_end)

        context = self.context.copy()
        context.update({
            'statistic_of_type_tickets': statistic_of_type_tickets,
            'count_tickets': statistic_of_type_tickets.count_tickets,
            'count_not_correct_localisation':
                statistic_of_type_tickets.count_not_correct_localisation,
            'count_not_correct_perform':
                statistic_of_type_tickets.count_not_correct_perform,
            'statistic_of_localisation':
                statistic_of_type_tickets.statistic_of_localisation,
            'statistic_of_perform':
                statistic_of_type_tickets.statistic_of_perform,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)


class WrongedTicketsView(DefaultContextMixin, GetPeriodMixin, LoginRequiredMixin, View):
    template_name = 'sugar_crm/wronged_tickets.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period()
        wronged_tickets = fetch_wronged_tickets(date_begin, date_end)

        context = self.context.copy()
        context.update({
            'wronged_tickets': wronged_tickets,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)


class MassTicketsView(DefaultContextMixin, GetPeriodMixin, LoginRequiredMixin, View):
    template_name = 'sugar_crm/mass_tickets.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period()
        mass_tickets = fetch_mass_tickets(date_begin, date_end)

        context = self.context.copy()
        context.update({
            'mass_tickets': mass_tickets,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)


class WrongedMassTicketsView(DefaultContextMixin, GetPeriodMixin, LoginRequiredMixin, View):
    template_name = 'sugar_crm/wronged_mass_tickets.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period()
        mass_tickets = fetch_wronged_mass_tickets(date_begin, date_end)

        context = self.context.copy()
        context.update({
            'mass_tickets': mass_tickets,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)


class TopTicketsView(DefaultTicketsViewMixin, View):
    template_name = 'sugar_crm/top_tickets.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period('month')
        top_tickets = fetch_top_tickets(date_begin, date_end)

        context = self.context.copy()
        context.update({
            'top_tickets': top_tickets,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)


class TopCallsView(DefaultTicketsViewMixin, View):
    template_name = 'sugar_crm/top_calls.html'

    @access_group('service')
    def get(self, request, *args, **kwargs):
        date_begin, date_end = self.get_period()
        top_calls = fetch_top_calls_to_support(date_begin, date_end)

        context = self.context.copy()
        context.update({
            'top_calls': top_calls,
            'date_begin': date_begin,
            'date_end': date_end,
        })
        return render(request, self.template_name, context)

from django.views.generic import View
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from utils.helpers import get_report_begin_end_date
from utils.helpers import get_report_periods
from utils.helpers import get_last_years, get_last_months
from utils.auth import access_group

from utm_billing.utm_utils.utm_pay_statistic import fetch_pays_from_utm, calculate_pays_stat_periods
from utm_billing.utm_utils.utm_pay_statistic import calculate_summary_statistic_pays
from utm_billing.utm_utils.utm_block_users import fetch_blocked_users_at_month


class PayStatisticView(LoginRequiredMixin, View):
    template_name = 'utm_billing/pay_statistic.html'
    login_url = reverse_lazy('login')

    @access_group('finance')
    def get(self, request, *args, **kwargs):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        last = self.kwargs.get('last', 'year')

        date_begin, date_end = get_report_begin_end_date(year, month, last)
        pays = fetch_pays_from_utm(date_begin, date_end)
        report_periods = get_report_periods(date_begin, date_end)
        pays_stat_periods = calculate_pays_stat_periods(pays, report_periods)
        pays_stat_summary = calculate_summary_statistic_pays(
            pays_stat_periods, report_periods, last)

        months_report = get_last_months(last=12)
        years_report = get_last_years(last=5)

        context = {
            'pays_stat': pays_stat_periods,
            'pays_stat_summary': pays_stat_summary,
            'months': months_report,
            'years': years_report,
            'type_report': 'pays_users',
            'date_begin': date_begin,
            'date_end': date_end,
        }
        return render(request, self.template_name, context)


class PayMonthStatisticView(PayStatisticView):
    template_name = "utm_billing/pay_month_statistic.html"


class BlockUsersMonth(LoginRequiredMixin, View):
    template_name = "utm_billing/block_users_month.html"
    login_url = reverse_lazy('login')

    @access_group('service')
    def get(self, request, *args, **kwargs):

        year = self.kwargs.get('year')
        month = self.kwargs.get('month')

        date_start, date_stop = get_report_begin_end_date(
            year, month, last='full_month')

        if not (date_start or date_stop):
            raise Http404('Не корректный url')

        block_users = fetch_blocked_users_at_month(date_start, date_stop)
        months_report = get_last_months(last=12)

        context = {
            'block_users': block_users,
            'date_begin': date_start,
            'months': months_report,
            'type_report': 'block_users',
        }

        return render(request, self.template_name, context)

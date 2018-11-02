from django.views.generic import TemplateView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from .helpers import get_report_begin_end_date
from .helpers import get_report_periods
from .helpers import get_last_years, get_last_months

from .utm_pay_statistic import fetch_pays_from_utm, calculate_pays_stat_periods
from .utm_pay_statistic import calculate_summary_statistic_pays
from .utm_block_users import fetch_blocked_users_at_month


class GetContextPayStatisticMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = kwargs.get('year')
        month = kwargs.get('month')
        last = kwargs.get('last', 'year')

        date_begin, date_end = get_report_begin_end_date(year, month, last)
        pays = fetch_pays_from_utm(date_begin, date_end)
        report_periods = get_report_periods(date_begin, date_end)
        pays_stat_periods = calculate_pays_stat_periods(pays, report_periods)
        pays_stat_summary = calculate_summary_statistic_pays(
            pays_stat_periods, report_periods, last)

        months_report = get_last_months(last=12)
        years_report = get_last_years(last=5)

        context_current = {
            'pays_stat': pays_stat_periods,
            'pays_stat_summary': pays_stat_summary,
            'months': months_report,
            'years': years_report,
            'type_report': 'pays_users',
            'date_begin': date_begin,
            'date_end': date_end,
        }

        context.update(context_current)
        return context


class PayStatisticView(GetContextPayStatisticMixin, LoginRequiredMixin, TemplateView):
    template_name = "utm_billing/pay_statistic.html"
    login_url = '/accounts/login/'


class PayMonthStatisticView(GetContextPayStatisticMixin, LoginRequiredMixin, TemplateView):
    template_name = "utm_billing/pay_month_statistic.html"
    login_url = '/accounts/login/'


class BlockUsersMonth(TemplateView, LoginRequiredMixin):
    template_name = "utm_billing/block_users_month.html"
    login_url = '/accounts/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = kwargs.get('year')
        month = kwargs.get('month')

        date_start, date_stop = get_report_begin_end_date(
            year, month, last='full_month')

        if not (date_start or date_stop):
            raise Http404('Не корректный url')

        block_users = fetch_blocked_users_at_month(date_start, date_stop)
        months_report = get_last_months(last=12)

        context_current = {
            'block_users': block_users,
            'date_begin': date_start,
            'months': months_report,
            'type_report': 'block_users',
        }

        context.update(context_current)
        return context

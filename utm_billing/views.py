from django.views.generic import TemplateView

from .helpers import get_report_begin_end_date
from .helpers import get_report_periods, get_type_report
from .helpers import get_last_years, get_last_months

from .utm_pay_statistic import fetch_pays_from_utm, calculate_pays_stat_periods
from .utm_pay_statistic import calculate_summary_statistic_pays


class PayStatisticView(TemplateView):
    template_name = "utm_billing/pay_statistic.html"

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
            pays_stat_periods, report_periods, last
        )

        # Формируем переменные для меню шаблона
        months_report = get_last_months(last=12)
        years_report = get_last_years(last=5)
        type_report = get_type_report(year, month)

        context_current = {
            'pays_stat': pays_stat_periods,
            'pays_stat_summary': pays_stat_summary,
            'months': months_report,
            'years': years_report,
            'type': type_report,
            'date_begin': date_begin,
            'date_end': date_end,
        }

        context.update(context_current)
        return context


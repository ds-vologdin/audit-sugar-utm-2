from utils.helpers import get_report_begin_end_date
from utils.helpers import get_last_years, get_last_months


class DefaultContextMixin:
    last_types = [
        ('week', 'Последняя неделя'), ('month', 'Последние 30 дней'),
        ('quarter', 'Последние 90 дней'), ('year', 'Последний год'),
        ('2years', 'Последние 2 года'), ('3years', 'Последние 3 года')
    ]
    context = {
        'months': get_last_months(last=6),
        'years': get_last_years(last=2),
        'last_types': last_types,
    }


class GetPeriodMixin:
    def get_period(self, default='week'):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        last = self.kwargs.get('last', default)

        return get_report_begin_end_date(year, month, last)

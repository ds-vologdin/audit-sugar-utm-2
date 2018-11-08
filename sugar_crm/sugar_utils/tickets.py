from datetime import timedelta

from sqlalchemy import func

from sugar_crm.database import session_crm
from sugar_crm.models import Bug, BugsCstm


def fill_empty_dates_in_statistic(statistic, date_begin, date_end, default=0):
    dates = [
        date_begin + timedelta(days=i) for i in range((date_end - date_begin).days)
    ]
    count_created_tickets = []
    i = 0
    for current_date in dates:
        _date, _stat = statistic[i]
        if current_date == _date:
            count_created_tickets.append((current_date, _stat))
            i += 1
        else:
            count_created_tickets.append((current_date, default))
    return count_created_tickets


def fetch_count_created_tickets_at_period(date_begin, date_end):
    count_created_tickets_at_period = session_crm.query(
        func.date(Bug.date_entered).label('report_date'),
        func.count(Bug.id)
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') <= date_end
    ).group_by('report_date').all()

    if len(count_created_tickets_at_period) != (date_end - date_begin).days:
        return fill_empty_dates_in_statistic(
            count_created_tickets_at_period, date_begin, date_end)

    return count_created_tickets_at_period


def is_opened_ticket_at_date(ticket, current_date):
    if ticket[2] is None and ticket[3] == 'open':
        return True
    if ticket[2] is None:
        return False
    if ticket[2].date() > current_date:
        return True
    return False


def calculate_statistic_of_open_tickets(tickets, periods):
    statistic_of_opened_tickets = {}
    for ticket in tickets:
        for current_date in periods:
            if ticket[1].date() > current_date:
                break
            if not is_opened_ticket_at_date(ticket, current_date):
                continue
            statistic_at_current_date = statistic_of_opened_tickets.get(
                current_date,
                {'all': 0, 'tp': 0, 'pd': 0, 'rs': 0, 'tf': 0, 'VNTV': 0}
            )
            statistic_at_current_date['all'] = statistic_at_current_date.get(
                'all', 0) + 1
            statistic_at_current_date[ticket[4]] = statistic_at_current_date.get(
                ticket[4], 0) + 1
            statistic_of_opened_tickets[current_date] = statistic_at_current_date
    ordered_statistic_of_opened_tickets = [
        (current_date, statistic_of_opened_tickets[current_date])
        for current_date in sorted(statistic_of_opened_tickets.keys())
    ]
    return ordered_statistic_of_opened_tickets


def get_statistic_of_opened_tickets(date_begin, date_end):
    opened_tickets = session_crm.query(
        Bug.bug_number, func.convert_tz(Bug.date_entered, '+00:00', '+03:00'),
        func.convert_tz(BugsCstm.date_close_c, '+00:00', '+03:00'),
        BugsCstm.status_bugs_c, BugsCstm.department_bugs_c
    ).join(
        BugsCstm, Bug.id == BugsCstm.id_c
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') <= date_end
    ).order_by(Bug.date_entered).all()

    periods = [
        date_end - timedelta(days=i) for i in range((date_end - date_begin).days + 1)
    ]

    ordered_statistic_of_opened_tickets = calculate_statistic_of_open_tickets(
        opened_tickets, periods)

    return ordered_statistic_of_opened_tickets


def get_statistic_of_type_tickets(date_begin, date_end):
    ...

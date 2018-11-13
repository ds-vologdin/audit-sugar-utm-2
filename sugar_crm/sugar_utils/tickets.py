from datetime import timedelta
from collections import namedtuple

from sqlalchemy import func

from sugar_crm.database import session_crm
from sugar_crm.models import Bug, BugsCstm
from .sugar_crm_dicts import BUG_LOCALISATION, BUG_PERFORM


StatisticOfTypeTickets = namedtuple(
    'StatisticOfTypeTickets',
    (
        'count_tickets',
        'count_not_correct_localisation',
        'count_not_correct_perform',
        'statistic_of_localisation',
        'statistic_of_perform'
    )
)


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


def parse_types(types):
    if types:
        return types.split(',')
    return ['^none^']


def update_statistic_of_types(statistic, types_in_str):
    """
    Dirty function!!! Function update statistic
    """
    types = parse_types(types_in_str)
    for current_type in types:
        statistic[current_type] = statistic.get(current_type, 0) + 1
    return statistic


def organize_statistic(statistic, count_tickets, name_dict):
    ordered_statistic_of_localisation = []
    for type_localisation, count in sorted(
            statistic.items(), key=lambda x: x[1], reverse=True):
        ordered_statistic_of_localisation.append({
            'type': type_localisation.replace('^', ''),
            'name': name_dict.get(type_localisation, type_localisation),
            'count': count,
            'percent': count * 100 / count_tickets,
        })
    return ordered_statistic_of_localisation


def get_statistic_of_type_tickets(date_begin, date_end):
    tickets = session_crm.query(
        Bug.bug_number, BugsCstm.perform_c, BugsCstm.localisation_c
    ).join(
        BugsCstm, Bug.id == BugsCstm.id_c
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end,
    ).all()

    statistic_of_localisation = {}
    statistic_of_perform = {}
    for ticket in tickets:
        update_statistic_of_types(statistic_of_perform, ticket[1])
        update_statistic_of_types(statistic_of_localisation, ticket[2])

    ordered_statistic_of_localisation = organize_statistic(
        statistic_of_localisation, len(tickets), BUG_LOCALISATION)
    ordered_statistic_of_perform = organize_statistic(
        statistic_of_perform, len(tickets), BUG_PERFORM)

    return StatisticOfTypeTickets(
        len(tickets),
        statistic_of_localisation.get('^none^'),
        statistic_of_perform.get('^none^'),
        ordered_statistic_of_localisation,
        ordered_statistic_of_perform
    )

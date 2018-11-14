from datetime import timedelta
from collections import namedtuple

from sqlalchemy import func, and_, or_

from sugar_crm.database import session_crm
from sugar_crm.models import Bug, BugsCstm, AccountsBug, Account, AccountsCstm
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
WrongedTicket = namedtuple(
    'WrongedTicket',
    ('id', 'bug_number', 'date_entered', 'date_close', 'department', 'status',
     'perform', 'localisation', 'duration')
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


def translate_types(types_in_str, dictionary):
    types = parse_types(types_in_str)
    return [dictionary.get(current_type, current_type) for current_type in types]


def fetch_wronged_tickets(date_begin, date_end):
    wronged_tickets = session_crm.query(
        Bug.id, Bug.bug_number, Bug.date_entered, BugsCstm.date_close_c,
        BugsCstm.department_bugs_c, BugsCstm.status_bugs_c, BugsCstm.perform_c,
        BugsCstm.localisation_c,
        BugsCstm.duration_bug_c + BugsCstm.duration_min_c/60
    ).join(
        BugsCstm, Bug.id == BugsCstm.id_c
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end,
        Bug.deleted == 0,
        BugsCstm.status_bugs_c != 'open',
        and_(
            or_(
                BugsCstm.perform_c == None, BugsCstm.perform_c == '',
                BugsCstm.perform_c == '^none^', BugsCstm.localisation_c == None,
                BugsCstm.localisation_c == '', BugsCstm.localisation_c == '^none^'
            )
        )
    ).order_by(Bug.date_entered).all()
    readable_wronged_tickets = []
    for ticket in wronged_tickets:
        _ticket = WrongedTicket(
            ticket[0], ticket[1], ticket[2], ticket[3], ticket[4], ticket[5],
            translate_types(ticket[6], BUG_PERFORM),
            translate_types(ticket[7], BUG_LOCALISATION), ticket[8]
        )
        readable_wronged_tickets.append(_ticket)
    return readable_wronged_tickets


def fetch_mass_tickets(date_begin, date_end):
    tickets = session_crm.query(
        Bug.id, Bug.bug_number, Bug.date_entered, Bug.name, Bug.description,
        BugsCstm.status_bugs_c, BugsCstm.address_bugs_c,
        BugsCstm.reason_for_closure_bugs_c,
        BugsCstm.duration_bug_c + BugsCstm.duration_min_c / 60,
        AccountsBug.account_id, Account.name, Account.billing_address_street,
        AccountsCstm.month_profit_acc_c
    ).join(
        BugsCstm, BugsCstm.id_c == Bug.id
    ).join(
        AccountsBug, AccountsBug.bug_id == Bug.id
    ).join(
        Account, Account.id == AccountsBug.account_id
    ).join(
        AccountsCstm, Account.id == AccountsCstm.id_c
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end,
        Bug.deleted == 0,
    ).order_by(Bug.date_entered).all()

    AccountInTicket = namedtuple('Account', ('id', 'name', 'address', 'payment'))
    MassTickets = namedtuple(
        'MassTicket',
        ('id', 'bug_number', 'date_entered', 'name', 'description', 'status',
         'address', 'close', 'duration', 'accounts', 'payment')
    )

    # Группируем таблицу по id, привязанных абонентов собираем в список
    # Это не красивое решение, но к сожалению в mysql нет типа array
    grouped_tickets = {}
    for ticket in tickets:
        account = AccountInTicket(*ticket[9:13])
        if ticket[0] not in grouped_tickets:
            accounts = [account]
            payment = account.payment
        else:
            accounts = grouped_tickets[ticket[0]].accounts
            accounts.append(account)
            payment = grouped_tickets[ticket[0]].payment + account.payment
        grouped_tickets[ticket[0]] = MassTickets(*ticket[0:9], accounts, payment)

    mass_tickets = []
    for ticket in grouped_tickets.values():
        if len(ticket.accounts) > 1:
            mass_tickets.append(MassTickets._make(ticket))
    return mass_tickets


def is_found_account_in_line(account, line):
    # Ищем в начале строки название организации
    found_acc = line[:10 + len(account)].find(account)
    if found_acc == -1:
        return False

    # С целью уменьшения ложных срабатываний проверяем, что после названия
    # организации стоит пробел, точка, запятая или строка уже кончилась
    end_char = found_acc + len(account)
    if not (line[end_char:end_char + 1] == '' or
            line[end_char:end_char + 1] == ' ' or
            line[end_char:end_char + 1] == '.' or
            line[end_char:end_char + 1] == ','):
        return False

    # Перед названием организации должен быть пробел, или это начало строки
    if not (found_acc == 0 or line[found_acc - 1:found_acc] == ' '):
        return False
    return True


def is_found_account_in_description(account, description):
    account = account.lower().replace(',', '').replace(
        'ооо', '').replace('зао', '').replace('ип', '').strip()
    if (account == 'точка' or account == 'мария' or
        account == 'статус' or account == 'объект' or
            account == 'виктория'):
        # Это особые организации, которые создаёт кучу ложных
        # срабатываний, поэтому сразу говорим, что ничего не нашли...
        return False

    # Переформатируем description
    description = description.lower().replace(',', '').replace(
        '\r', '').replace('(', ' ').replace(')', ' ').replace(
        '"', ' ').replace('\'', ' ')
    for line in description.splitlines():
        if is_found_account_in_line(account, line):
            # если контрагент найден, дальше строки смотреть не надо
            return True
    return False


def fetch_wronged_mass_tickets(date_begin, date_end):
    tickets = session_crm.query(
        Bug.id, Bug.bug_number, Bug.date_entered, Bug.name, Bug.description,
        AccountsBug.account_id, Account.name
    ).join(
        AccountsBug, AccountsBug.bug_id == Bug.id
    ).join(
        Account, Account.id == AccountsBug.account_id
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end,
        Bug.deleted == 0,
        Bug.description != None
    ).order_by(Bug.date_entered).all()

    AccountInTicket = namedtuple('Account', ('id', 'name'))
    MassTickets = namedtuple(
        'WrongedMassTickets',
        ('id', 'bug_number', 'date_entered', 'name', 'description',
         'accounts', 'not_fixed_accounts')
    )

    # Группируем таблицу по id, привязанных абонентов собираем в список
    # Это не красивое решение, но к сожалению в mysql нет типа array
    grouped_tickets = {}
    for ticket in tickets:
        account = AccountInTicket(*ticket[5:7])
        if ticket[0] not in grouped_tickets:
            accounts = [account]
            grouped_tickets[ticket[0]] = MassTickets(*ticket[0:5], accounts, [])
        else:
            grouped_tickets[ticket[0]].accounts.append(account)

    accounts = session_crm.query(
        Account.id, Account.name
    ).join(
        AccountsCstm, Account.id == AccountsCstm.id_c
    ).filter(
        AccountsCstm.status_acc_c == 'active',
        AccountsCstm.company_acc_c == 1,
        Account.deleted == 0
    ).all()

    # Ищем тикеты, в описании которых есть упоминания названий абонентов,
    # не привязанных к тикету
    tickets_with_not_fixed_accounts = []
    for ticket in grouped_tickets.values():
        ticket_account_ids = set([account.id for account in ticket.accounts])
        for account_id, account_name in accounts:
            if account_id in ticket_account_ids:
                continue
            if is_found_account_in_description(account_name, ticket.description):
                ticket.not_fixed_accounts.append(AccountInTicket(
                    account_id, account_name))
        if ticket.not_fixed_accounts:
            tickets_with_not_fixed_accounts.append(ticket)

    wronged_tickets = [
        ticket for ticket in tickets_with_not_fixed_accounts if ticket.not_fixed_accounts
    ]
    return wronged_tickets

from datetime import timedelta
from collections import namedtuple

from sqlalchemy import func, and_, or_, desc

from sugar_crm.database import session_crm
from sugar_crm.models import Bug, BugsCstm, AccountsBug, Account, AccountsCstm
from sugar_crm.models import Call, AccountsCalls1C
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
MassTickets = namedtuple(
    'MassTicket',
    ('id', 'bug_number', 'date_entered', 'name', 'description', 'status',
     'address', 'close', 'duration', 'accounts', 'payment')
)
WrongedMassTickets = namedtuple(
    'WrongedMassTickets',
    ('id', 'bug_number', 'date_entered', 'name', 'description',
     'accounts', 'not_fixed_accounts')
)
AccountInTicket = namedtuple('Account', ('id', 'name', 'address', 'payment'))
AccountInTicketLite = namedtuple('AccountLite', ('id', 'name'))
TopTicket = namedtuple('TopTicket', ('account', 'count', 'tickets', 'tickets_other'))
TicketLite = namedtuple('TicketLite', ('id', 'bug_number', 'date_entered'))
TopCall = namedtuple('TopCall', ('phone', 'count', 'account', 'tickets'))
NoServiceTicket = namedtuple(
    'NoServiceTicket',
    ('id', 'bug_number', 'date_entered', 'duration', 'accounts')
)

INTERNAL_PHONES = ('226001', '226002', '226333', '227485', '227012',
                   '226012', '227081', '226081')


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


def is_found_account_in_description(account, description_lines):
    account = account.lower().replace(',', '').replace(
        'ооо', '').replace('зао', '').replace('ип', '').strip()
    if (account == 'точка' or account == 'мария' or
        account == 'статус' or account == 'объект' or
            account == 'виктория'):
        # Это особые организации, которые создаёт кучу ложных
        # срабатываний, поэтому сразу говорим, что ничего не нашли...
        return False

    for line in description_lines:
        if is_found_account_in_line(account, line):
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

    # Группируем таблицу по id, привязанных абонентов собираем в список
    # Это не красивое решение, но к сожалению в mysql нет типа array
    grouped_tickets = {}
    for ticket in tickets:
        account = AccountInTicketLite(*ticket[5:7])
        if ticket[0] not in grouped_tickets:
            accounts = [account]
            grouped_tickets[ticket[0]] = WrongedMassTickets(*ticket[0:5], accounts, [])
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
        ticket_account_ids = set(account.id for account in ticket.accounts)
        # Чистим описание тикета от любымих символов саппорта
        description = ticket.description.lower().replace(',', '').replace(
            '\r', '').replace('(', ' ').replace(')', ' ').replace(
            '"', ' ').replace('\'', ' ')
        description_lines = description.splitlines()
        for account_id, account_name in accounts:
            if account_id in ticket_account_ids:
                continue
            if is_found_account_in_description(account_name, description_lines):
                ticket.not_fixed_accounts.append(AccountInTicketLite(
                    account_id, account_name))
        if ticket.not_fixed_accounts:
            tickets_with_not_fixed_accounts.append(ticket)

    wronged_tickets = [
        ticket for ticket in tickets_with_not_fixed_accounts if ticket.not_fixed_accounts
    ]
    return wronged_tickets


def fetch_tickets_of_account_ids(account_ids, date_begin=None, date_end=None):
    tickets_query = session_crm.query(
        Bug.id, Bug.bug_number, Bug.date_entered, AccountsBug.account_id
    ).join(
        AccountsBug, Bug.id == AccountsBug.bug_id
    ).filter(
        AccountsBug.account_id.in_(account_ids)
    ).order_by(Bug.date_entered)
    if date_begin:
        tickets_query = tickets_query.filter(
            func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin)
    if date_end:
        tickets_query = tickets_query.filter(
            func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end)
    tickets_raw = tickets_query.all()

    tickets = {}
    for ticket in tickets_raw:
        account_id = ticket[3]
        if account_id in tickets:
            tickets[account_id].append(TicketLite(*ticket[:3]))
        else:
            tickets[account_id] = [TicketLite(*ticket[:3])]
    return tickets


def fetch_top_tickets(date_begin, date_end, top=50):
    top_tickets_raw = session_crm.query(
        Account.id, Account.name,  Account.billing_address_street,
        AccountsCstm.month_profit_acc_c, func.count(AccountsBug.id).label('count')
    ).join(
        AccountsCstm, Account.id == AccountsCstm.id_c
    ).join(
        AccountsBug, Account.id == AccountsBug.account_id
    ).join(
        Bug, AccountsBug.bug_id == Bug.id
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end,
        Bug.deleted == 0,
        AccountsBug.account_id != '90657094-4fdd-9c4c-dc07-559b8ff0c6ea',
        AccountsBug.account_id != '581c9d33-2f3f-88e3-9d28-55e052c92010',
    ).group_by(Account.id).order_by(desc('count')).limit(top).all()

    top_tickets = []
    account_ids = []
    for ticket in top_tickets_raw:
        top_tickets.append(TopTicket(AccountInTicket(*ticket[:4]), ticket[4], [], []))
        account_ids.append(ticket[0])

    tickets_of_account_ids = fetch_tickets_of_account_ids(account_ids)

    for ticket in top_tickets:
        tickets_account = tickets_of_account_ids.get(ticket.account.id, [])
        for ticket_account in tickets_account:
            if date_begin <= ticket_account.date_entered.date() < date_end:
                ticket.tickets.append(ticket_account)
            else:
                ticket.tickets_other.append(ticket_account)
    return top_tickets


def fetch_top_calls_to_support(date_begin, date_end, top=50):
    calls_to_support_raw = session_crm.query(
        func.substring_index(
            func.substring_index(Call.name, ' ', -3), ' ', 1).label('from_number'),
        func.count(Call.id).label('count'),
        AccountsCalls1C.accounts_calls_1accounts_ida,
        Account.name, Account.billing_address_street,
        AccountsCstm.month_profit_acc_c,
    ).outerjoin(
        AccountsCalls1C, Call.id == AccountsCalls1C.accounts_calls_1calls_idb
    ).outerjoin(
        Account, AccountsCalls1C.accounts_calls_1accounts_ida == Account.id
    ).outerjoin(
        AccountsCstm, Account.id == AccountsCstm.id_c
    ).filter(
        func.convert_tz(Call.date_start, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Call.date_start, '+00:00', '+03:00') < date_end,
        Call.direction == 'Inbound',
        Call.status == 'autoheld',
        Call.created_by == "9daf7540-986e-8385-7040-55b63cc60145",
        ~func.substring_index(
            func.substring_index(Call.name, ' ', -3), ' ', 1
        ).label('from_number').in_(INTERNAL_PHONES)
    ).group_by('from_number').order_by(desc('count')).limit(top).all()

    calls_to_support = []
    account_ids = []
    for call in calls_to_support_raw:
        if call[2]:
            calls_to_support.append(
                TopCall(*call[:2], AccountInTicket(*call[2:6]), []))
            account_ids.append(call[2])
        else:
            calls_to_support.append(TopCall(*call[:2], None, None))

    tickets_of_account_ids = fetch_tickets_of_account_ids(
        account_ids, date_begin, date_end)
    for call in calls_to_support:
        if not call.account:
            continue
        tickets = tickets_of_account_ids.get(call.account.id)
        if tickets:
            call.tickets.extend(tickets)
    return calls_to_support


def calc_ticket_duration(hours, minutes):
    result = 0
    if hours:
        result += hours
    if minutes:
        result += minutes/60
    return result


def fetch_tickets_with_stop_service(date_begin, date_end):
    AccountInTicketStopService = namedtuple(
        'Account', ('id', 'name', 'address', 'payment', 'company'))

    tickets_raw = session_crm.query(
        Bug.id, Bug.bug_number, Bug.date_entered, BugsCstm.duration_bug_c,
        BugsCstm.duration_min_c, Account.id, Account.name,
        Account.billing_address_street, AccountsCstm.month_profit_acc_c,
        AccountsCstm.company_acc_c
    ).join(
        BugsCstm, BugsCstm.id_c == Bug.id
    ).join(
        AccountsBug, AccountsBug.bug_id == Bug.id
    ).join(
        Account, AccountsBug.account_id == Account.id
    ).join(
        AccountsCstm, AccountsCstm.id_c == Account.id
    ).filter(
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') >= date_begin,
        func.convert_tz(Bug.date_entered, '+00:00', '+03:00') < date_end,
        or_(BugsCstm.duration_bug_c > 0, BugsCstm.duration_min_c > 0)
    ).all()

    tickets = {}
    for ticket in tickets_raw:
        ticket_id = ticket[0]
        if ticket_id == '90657094-4fdd-9c4c-dc07-559b8ff0c6ea':
            # фильтруем лишнее
            continue
        duration = calc_ticket_duration(ticket[3], ticket[4])
        account = AccountInTicketStopService(*ticket[5:9], ticket[9])
        if ticket_id in tickets:
            tickets[ticket_id].accounts.append(account)
        else:
            tickets[ticket_id] = NoServiceTicket(
                *ticket[:3], duration, [account])
    return tickets.values()


def get_top_account_with_stop_service(tickets, period_in_hours):
    NoServiceAccount = namedtuple(
        'NoServiceAccount', ('account', 'tickets', 'duration', 'availability'))
    TicketNoService = namedtuple('TicketLite', ('id', 'bug_number', 'duration'))
    account_stop_duration = {}
    for ticket in tickets:
        _ticket = TicketNoService(ticket.id, ticket.bug_number, ticket.duration)
        for account in ticket.accounts:
            if account.id in account_stop_duration:
                _account = account_stop_duration[account.id]
                _tickets = _account.tickets
                duration = _account.duration
            else:
                _tickets = []
                duration = 0
            _tickets.append(_ticket)

            duration += ticket.duration
            availability = (period_in_hours - duration) / period_in_hours

            account_stop_duration[account.id] = NoServiceAccount(
                account, _tickets, duration, availability)
    return sorted(
        account_stop_duration.values(), key=lambda x: x.duration, reverse=True)

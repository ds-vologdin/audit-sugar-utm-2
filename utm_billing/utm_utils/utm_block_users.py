from datetime import datetime, date, timedelta
import pytz
from collections import namedtuple

from utils.helpers import get_timestamp_from_date
from utm_billing.database import session_utm
from utm_billing.models import User, BlocksInfo, ServiceLink, ServicesDatum
from utm_billing.models import TariffsHistory


BlockedUser = namedtuple(
    'BlockedUser', ['id', 'login', 'name', 'address', 'phone', 'block_date'])

BlockedUserTariff = namedtuple(
    'BlockedUser', ['id', 'login', 'name', 'address', 'phone', 'block_date', 'tariff'])


def fetch_blocked_users(block_date_start=None, block_date_stop=None):
    """ Функция возвращает список заблокированных пользователей """
    timestamp_expire = get_timestamp_from_date(date(2030, 1, 1))

    blocked_users_query = session_utm.query(
        User.id, User.login, User.full_name, User.actual_address,
        User.mobile_telephone, BlocksInfo.start_date.label('block_date')
    ).join(
        BlocksInfo, User.basic_account == BlocksInfo.account_id
    ).filter(
        BlocksInfo.expire_date > timestamp_expire,
        User.login.op('~')('^\d\d\d\d\d$')
    ).distinct(User.id).order_by(User.id)

    if block_date_start:
        timestamp_begin = get_timestamp_from_date(block_date_start)
        blocked_users_query = blocked_users_query.filter(
            BlocksInfo.start_date >= timestamp_begin)
    if block_date_stop:
        timestamp_end = get_timestamp_from_date(
            block_date_stop + timedelta(days=1))
        blocked_users_query = blocked_users_query.filter(
            BlocksInfo.start_date < timestamp_end)

    blocked_users_query = blocked_users_query.cte()
    blocked_users_query_ordered = session_utm.query(
        blocked_users_query
    ).order_by(blocked_users_query.c.block_date)
    blocked_users = [
        BlockedUser._make(user) for user in list(blocked_users_query_ordered)
    ]
    return blocked_users


def fetch_blocked_users_at_month(block_date_start, block_date_stop):
    """
    Функция для получения данных по блокировке пользователей UTM
    в промежутке между block_date_start и block_date_stop
    """
    blocked_users = fetch_blocked_users(block_date_start, block_date_stop)
    user_ids = [user.id for user in blocked_users]

    # Запрашиваем активные сервисные связки
    services_user = session_utm.query(
        User.id, ServicesDatum.service_name, ServicesDatum.comment,
        ServicesDatum.id
    ).join(
        ServiceLink, User.basic_account == ServiceLink.account_id
    ).join(
        ServicesDatum, ServiceLink.service_id == ServicesDatum.id
    ).filter(
        User.id.in_(user_ids),
        ServicesDatum.is_deleted == 0,
        ServiceLink.is_deleted == 0,
        User.is_deleted == 0,
        ServicesDatum.id != 614
    ).order_by(User.id).all()

    blocked_users_info = []
    # Получаем тарифы пользователя и формируем список словарей с информацией
    # об ушёдшим в блок пользователям
    for user in blocked_users:
        services = [
            services_user for service_id, *services_user in services_user
            if service_id == user.id
        ]

        if not services:
            # Активных сервисных связок нет, запрашиваем историю тарифов
            tariff_history = session_utm.query(
                TariffsHistory.tariff_name, TariffsHistory.unlink_date
            ).join(
                User, TariffsHistory.account_id == User.basic_account
            ).filter(
                User.id == user.id
            ).order_by(TariffsHistory.unlink_date.desc()).all()
            service = tariff_history[0][0] if len(tariff_history) > 0 else ''
        else:
            # Есть активные сервисные связки
            service_names = [service[0] for service in services]
            service = '; '.join(service_names)
        blocked_users_info.append(BlockedUserTariff(
            id=user.id,
            login=user.login,
            name=user.name,
            address=user.address,
            phone=user.phone,
            block_date=datetime.fromtimestamp(
                user.block_date, tz=pytz.timezone('Europe/Moscow')),
            tariff=service,
        ))
    return blocked_users_info

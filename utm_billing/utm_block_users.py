from datetime import datetime, date, timedelta
import pytz

from .helpers import get_timestamp_from_date
from .database import session_utm
from .models import User, BlocksInfo, ServiceLink, ServicesDatum
from .models import TariffsHistory


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

    return list(blocked_users_query_ordered)


def fetch_blocked_users_at_month(block_date_start, block_date_stop):
    """
    Функция для получения данных по блокировке пользователей UTM
    в промежутке между block_date_start и block_date_stop
    """
    blocked_users = fetch_blocked_users(block_date_start, block_date_stop)
    user_ids = [block_id for block_id, *block in blocked_users]

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
    for block in blocked_users:
        services = [
            services_user for service_id, *services_user in services_user
            if service_id == block[0]
        ]

        if not services:
            # Активных сервисных связок нет, запрашиваем историю тарифов
            tariff_history = session_utm.query(
                TariffsHistory.tariff_name, TariffsHistory.unlink_date
            ).join(
                User, TariffsHistory.account_id == User.basic_account
            ).filter(
                User.id == block[0]
            ).order_by(TariffsHistory.unlink_date.desc()).all()
            service = tariff_history[0][0] if len(tariff_history) > 0 else ''
        else:
            # Есть активные сервисные связки
            service_names = [ser[0] for ser in services]
            service = '; '.join(service_names)
        blocked_users_info.append({
            'login': block[1],
            'user': block[2],
            'address': block[3],
            'phone': block[4],
            'date': datetime.fromtimestamp(
                block[5], tz=pytz.timezone('Europe/Moscow')),
            'tarif': service,
        })
    return blocked_users_info

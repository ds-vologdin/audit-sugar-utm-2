from collections import namedtuple
from datetime import datetime, timedelta
import pytz

from utm_billing.utm_utils.utm_block_users import fetch_blocked_users
from ..models import PoPo, PoPoCstm, Account, AccountsCstm
from ..database import session_crm
from .sugar_crm_dicts import HARDWARE_TYPES, STATUS_DEVICE


Hardware = namedtuple(
    'HardwareToRemove',
    ['name', 'description', 'status', 'type', 'type_id', 'inventory', 'login'])
UsersHardware = namedtuple(
    'UsersHardware', ['login', 'name', 'address', 'phone', 'block_date', 'hardware'])


def fetch_hardware_to_remove(date_end=None):
    if not date_end:
        date_end = (datetime.now() - timedelta(days=30)).replace(day=1)
    blocked_users = fetch_blocked_users(block_date_stop=date_end)

    users_login = [user.login for user in blocked_users]
    hardware_to_remove = session_crm.query(
        PoPo.name, PoPo.description, PoPoCstm.status_c,
        PoPoCstm.hardware_types_c, PoPoCstm.invnum_c,
        AccountsCstm.login_ph_c
    ).join(
        PoPoCstm, PoPo.id == PoPoCstm.id_c
    ).join(
        Account, Account.id == PoPoCstm.account_id_c
    ).join(
        AccountsCstm, Account.id == AccountsCstm.id_c
    ).filter(
        AccountsCstm.login_ph_c.in_(users_login)
    ).all()

    login_info_to_hardware = {}
    for _hardware in hardware_to_remove:
        hardware = Hardware(
            name=_hardware[0],
            description=_hardware[1],
            status=STATUS_DEVICE.get(_hardware[2], _hardware[2]),
            type=HARDWARE_TYPES.get(_hardware[3], _hardware[3]),
            type_id=_hardware[3],
            inventory=_hardware[4],
            login=_hardware[5],
        )
        devices = login_info_to_hardware.get(hardware.login, [])
        devices.append(hardware)
        login_info_to_hardware[hardware.login] = devices

    users_info_hardware = []
    for user in blocked_users:
        if user.login not in login_info_to_hardware:
            continue
        hardware = login_info_to_hardware.get(user.login)
        # Нас мало интересуют абонентские wi-fi
        if len(hardware) == 1 and hardware[0].type_id in ('101', '116', '1106'):
            continue
        users_info_hardware.append(UsersHardware(
            login=user.login,
            name=user.name,
            address=user.address,
            phone=user.phone,
            block_date=datetime.fromtimestamp(
                user.block_date, tz=pytz.timezone('Europe/Moscow')),
            hardware=hardware,
        ))
    return users_info_hardware

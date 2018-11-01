from collections import namedtuple
from datetime import datetime
import pytz

from utm_billing.utm_block_users import fetch_blocked_users
from ..models import PoPo, PoPoCstm, Account, AccountsCstm
from ..database import session_crm


Hardware = namedtuple(
    'HardwareToRemove', ['name', 'description', 'status', 'type', 'inventory', 'login'])
UsersHardware = namedtuple(
    'UsersHardware', ['login', 'name', 'address', 'phone', 'block_date', 'hardware'])


def fetch_hardware_to_remove():
    blocked_users = fetch_blocked_users()

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
        hardware = Hardware._make(_hardware)
        devices = login_info_to_hardware.get(hardware.login, [])
        devices.append(hardware)
        login_info_to_hardware[hardware.login] = devices

    users_info_hardware = []
    for user in blocked_users:
        if user.login not in login_info_to_hardware:
            continue
        users_info_hardware.append(UsersHardware(
            login=user.login,
            name=user.name,
            address=user.address,
            phone=user.phone,
            block_date=datetime.fromtimestamp(
                user.block_date, tz=pytz.timezone('Europe/Moscow')),
            hardware=login_info_to_hardware.get(user.login)
        ))
    return users_info_hardware

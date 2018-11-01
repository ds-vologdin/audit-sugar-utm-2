from django.views.generic import TemplateView

from utm_billing.utm_block_users import fetch_blocked_users
from .models import PoPo, PoPoCstm, Account, AccountsCstm
from .database import session_crm


class HardwareToRemove(TemplateView):
    template_name = "sugar_crm/hardware_to_remove.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blocked_users = fetch_blocked_users()

        users_login = [login for user_id, login, *_ in blocked_users]
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
        for *hw, login in hardware_to_remove:
            devices = login_info_to_hardware.get(login, [])
            devices.append(hw)
            login_info_to_hardware[login] = devices

        users_info_hardware = []
        for user in blocked_users:
            if user[1] not in login_info_to_hardware:
                continue
            login = user[1]
            users_info_hardware.append({
                'login': login,
                'name': user[2],
                'address': user[3],
                'phone': user[4],
                'block_date': user[5],
                'hardware': login_info_to_hardware.get(login)
            })

        context.update({
            'blocked_users': blocked_users,
            'hardware_to_remove': users_info_hardware,
            'type_report': 'hardware_to_remove',
        })

        return context

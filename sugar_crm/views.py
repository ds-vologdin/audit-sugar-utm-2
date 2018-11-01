from django.views.generic import TemplateView

from .utils.hardware_to_remove import fetch_hardware_to_remove


class HardwareToRemoveView(TemplateView):
    template_name = "sugar_crm/hardware_to_remove.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hardware_to_remove = fetch_hardware_to_remove()

        context.update({
            'hardware_to_remove': hardware_to_remove,
            'type_report': 'hardware_to_remove',
        })
        return context

from django.utils.translation import ugettext_lazy as _
import horizon


class DemoPanel(horizon.Panel):
    name = _("Demo Panel")
    slug = "demopanel"

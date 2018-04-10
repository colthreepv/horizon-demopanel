from django.utils.translation import ugettext_lazy as _
import horizon


class CatsPanel(horizon.Panel):
    name = _("Cats Panel")
    slug = "catspanel"

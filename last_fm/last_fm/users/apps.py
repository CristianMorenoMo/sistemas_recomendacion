from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "last_fm.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import last_fm.users.signals  # noqa F401
        except ImportError:
            pass

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'
    verbose_name = 'Accounts & Users'

    def ready(self):
        """Initialize signals when app is ready"""
        import accounts.signals  # noqa

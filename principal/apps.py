from django.apps import AppConfig


class PrincipalConfig(AppConfig):
    name = 'principal'

    def ready(self):
        import principal.receivers
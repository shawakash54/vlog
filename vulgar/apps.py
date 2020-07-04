from django.apps import AppConfig


class VulgarConfig(AppConfig):
    name = 'vulgar'

    def ready(self):
        import vulgar.signals

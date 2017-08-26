from django.apps import AppConfig


class EventsConfig(AppConfig):
    name = 'apps.events'
    verbose_name = '시그널 테스트를 위한 이벤트 앱'

    def ready(self):
        from apps.events import signals

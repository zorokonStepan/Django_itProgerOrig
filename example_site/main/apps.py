from django.apps import AppConfig

"""Настройки именно этого приложения"""


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

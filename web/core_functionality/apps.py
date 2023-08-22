from django.apps import AppConfig

from .ml_models_classes import RobertaBaseSquad2


class CoreFunctionalityConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_functionality'

    # def ready(self) -> None:
    ml_model = RobertaBaseSquad2()

from django.dispatch import receiver

from sports.services import SportsService
from events import signals


@receiver(signals.deactivate_sport)
def deactivate_sport(sender, sport_id, **kwargs):
    SportsService().update_sport(payload={'id': sport_id, 'active': False})

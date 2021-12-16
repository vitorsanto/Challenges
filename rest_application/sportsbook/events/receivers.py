from django.dispatch import receiver

from events.services import EventsService
from selections import signals


@receiver(signals.deactivate_event)
def deactivate_event(sender, event_id, **kwargs):
    EventsService().update_events(payload={'id': event_id, 'active': False})

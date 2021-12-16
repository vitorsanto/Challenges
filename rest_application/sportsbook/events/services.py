from rest_framework import status

from events.repositories import EventsRepository
from events import signals

class EventsService:

    def __init__(self):
        self.events_repository_class = EventsRepository
        self.deactivate_sport_signal = signals.deactivate_sport

    def create_events(self, payload):
        try:
            result = self.get_events_repository().create_event(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def update_events(self, payload):
        try:
            result = self.get_events_repository().update_event(payload)
            active_events = self.get_events_repository().events_active_from_sport(result[-1])
            if not active_events:
                self.deactivate_sport_signal.send(sender='update_events', sport_id=result[-1])
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def list_events(self, query_params):
        try:
            result = self.get_events_repository().list_events(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def check_event(self, pk):
        return self.get_events_repository().check_event(pk)

    def get_events_repository(self):
        return self.events_repository_class()

    def error_handling(self, e: Exception):
        return getattr(e, 'message', repr(e))

    def deactivate_event(self, pk):
        try:

            result = self.get_events_repository().deactivate_event(pk)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}
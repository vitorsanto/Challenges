from rest_framework import status

from selections import signals
from selections.repositories import SelectionsRepository


class SelectionsService:

    def __init__(self):
        self.selections_repository_class = SelectionsRepository
        self.deactivate_event_signal = signals.deactivate_event

    def create_selections(self, payload):
        try:
            result = self.get_selections_repository().create_selection(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def update_selections(self, payload):
        try:
            result = self.get_selections_repository().update_selection(payload)
            active_selections = self.get_selections_repository().selections_active_from_event(result[-1])
            if not active_selections:
                self.deactivate_event_signal.send(sender='update_selections', event_id=result[-1])
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def list_selections(self, query_params):
        try:
            result = self.get_selections_repository().list_selections(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def check_selection(self, pk):
        return self.get_selections_repository().check_selection(pk)

    def error_handling(self, e: Exception):
        return getattr(e, 'message', repr(e))

    def get_selections_repository(self):
        return self.selections_repository_class()

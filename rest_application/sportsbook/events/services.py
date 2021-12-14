from rest_framework import status

from events.repositories import EventsRepository


class EventsService:

    @staticmethod
    def create_events(payload):
        try:
            result = EventsRepository.create_event(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def update_events(payload):
        try:
            result = EventsRepository.update_event(payload)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def list_events(query_params):
        try:
            result = EventsRepository.list_events(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def fetch_event(pk):
        return EventsRepository.fetch_event(pk)

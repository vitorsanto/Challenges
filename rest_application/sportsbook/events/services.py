from rest_framework import status

from events.repositories import EventsRepository


class EventsService:

    @staticmethod
    def create_events(payload):
        result = EventsRepository.create_event(payload)
        return {'data': result, 'status': status.HTTP_201_CREATED}

    @staticmethod
    def update_events(payload):
        result = EventsRepository.update_event(payload)
        return {'data': result, 'status': status.HTTP_200_OK}

    @staticmethod
    def list_events(query_params):
        result = EventsRepository.list_events(query_params)
        return {'data': result, 'status': status.HTTP_200_OK}

    @staticmethod
    def fetch_event(pk):
        return EventsRepository.fetch_event(pk)

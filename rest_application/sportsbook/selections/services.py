from rest_framework import status

from selections.repositories import SelectionsRepository


class SelectionsService:

    @staticmethod
    def create_selections(payload):
        try:
            result = SelectionsRepository.create_selection(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def update_selections(payload):
        try:
            result = SelectionsRepository.update_selection(payload)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def list_selections(query_params):
        try:
            result = SelectionsRepository.list_selections(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def fetch_selection(pk):
        return SelectionsRepository.fetch_selection(pk)

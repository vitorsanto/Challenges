from rest_framework import status

from sports.repositories import SportsRepository


class SportsService:

    @staticmethod
    def create_sports(payload):
        try:
            result = SportsRepository.create_sport(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def update_sport(payload):
        try:
            result = SportsRepository.update_sport(payload)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def list_sports(query_params):
        try:
            result = SportsRepository.list_sports(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    @staticmethod
    def fetch_sport(pk):
        return SportsRepository.fetch_sport(pk)

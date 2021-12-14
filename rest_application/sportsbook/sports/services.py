from rest_framework import status

from sports.repositories import SportsRepository


class SportsService:

    @staticmethod
    def create_sports(payload):
        result = SportsRepository.create_sport(payload)
        return {'data': result, 'status': status.HTTP_201_CREATED}

    @staticmethod
    def update_sport(payload):
        result = SportsRepository.update_sport(payload)
        return {'data': result, 'status': status.HTTP_200_OK}

    @staticmethod
    def list_sports(query_params):
        result = SportsRepository.list_sports(query_params)
        return {'data': result, 'status': status.HTTP_200_OK}

    @staticmethod
    def fetch_sport(pk):
        return SportsRepository.fetch_sport(pk)

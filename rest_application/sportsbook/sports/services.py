from rest_framework import status

from sports.repositories import SportsRepository


class SportsService:
    sports_repository = SportsRepository

    def create_sports(self, payload):
        try:
            result = self.sports_repository.create_sport(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def update_sport(self, payload):
        try:
            result = self.sports_repository.update_sport(payload)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def list_sports(self, query_params):
        try:
            result = self.sports_repository.list_sports(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': self.error_handling(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def check_sport(self, pk):
        return self.sports_repository.check_sport(pk)

    def error_handling(self, e: Exception):
        return getattr(e, 'message', repr(e))

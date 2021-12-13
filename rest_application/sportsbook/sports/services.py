from rest_framework import status


class SportsService:

    @staticmethod
    def create_sports(payload):
        return {'data': payload, 'status': status.HTTP_201_CREATED}

    @staticmethod
    def update_sport(payload):
        return {'data': payload, 'status': status.HTTP_200_OK}

    @staticmethod
    def list_sports(payload):
        return {'data': payload, 'status': status.HTTP_200_OK}

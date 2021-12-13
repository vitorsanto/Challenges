from rest_framework import status


class SportsService:

    @staticmethod
    def create_sports(payload):
        return {'data': payload, 'status': status.HTTP_201_CREATED}

    @staticmethod
    def update_sport(payload):
        return {'data': payload, 'status': status.HTTP_200_OK}

    @staticmethod
    def list_sports(query_params):
        supported_filters = (
            'name',
            'name_regex',
            'active_events[lte]',
            'active_events[gte]',
            'is_active'
        )

        return {'data': query_params, 'status': status.HTTP_200_OK}

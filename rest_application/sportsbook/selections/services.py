from rest_framework import status

from selections.repositories import SelectionsRepository


class SelectionsService:
    selections_repository = SelectionsRepository

    def create_selections(self, payload):
        try:
            result = self.selections_repository.create_selection(payload)
            return {'data': result, 'status': status.HTTP_201_CREATED}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def update_selections(self, payload):
        try:
            result = self.selections_repository.update_selection(payload)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def list_selections(self, query_params):
        try:
            result = self.selections_repository.list_selections(query_params)
            return {'data': result, 'status': status.HTTP_200_OK}
        except Exception as e:
            return {'data': str(e), 'status': status.HTTP_500_INTERNAL_SERVER_ERROR}

    def check_selection(self, pk):
        return self.selections_repository.check_selection(pk)

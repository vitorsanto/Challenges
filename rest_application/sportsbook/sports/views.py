from rest_framework import generics
from rest_framework.response import Response

from sports.services import SportsService


class CreateSportsView(generics.GenericAPIView):
    """
    Create Sport
    """
    name = 'create-sports'

    def post(self, request, *args, **kwargs):
        response = SportsService.create_sports(request)
        return Response(response)


class UpdateSportsView(generics.GenericAPIView):
    """
    Update Sport
    """
    name = 'update-sports'

    def patch(self, request, *args, **kwargs):
        response = SportsService.update_sport(request)
        return Response(response)


class ListSportsView(generics.GenericAPIView):
    """
    List Sports
    """
    name = 'list-sports'

    def get(self, request, *args, **kwargs):
        response = SportsService.list_sport(request)
        return Response(response)

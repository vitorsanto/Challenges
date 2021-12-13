from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from sports.serializers import SportsSerializer
from sports.services import SportsService


class CreateSportsView(generics.GenericAPIView):
    """
    Create Sport
    """
    name = 'create-sports'
    serializer_class = SportsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = SportsService.create_sports(serializer.data)
            return Response(response['data'], status=response['status'])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

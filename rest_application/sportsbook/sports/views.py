from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from sports.serializers import CreateSportsSerializer, ListSportsSerializer, UpdateSportsSerializer
from sports.services import SportsService


class CreateSportsView(generics.GenericAPIView):
    """
     #Create Sports
     Create a sport.

     ---

     ##Params:

     * **name (str)**: Sport name.

     * **active (int)**: Sport active.

     """
    name = 'create-sports'
    serializer_class = CreateSportsSerializer
    sports_service = SportsService

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = self.get_sports_service().create_sports(serializer.data)
            return Response(response['data'], status=response['status'])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_sports_service(self):
        return self.sports_service()


class UpdateSportsView(generics.GenericAPIView):
    """
    #Update Sports
    Update a sport.

    ---

    ##Params:

    * **ID (int)**: Sport's instance ID .

    * **name (str)**: Patch name.

    * **active (int)**: Patch active.

    """
    name = 'update-sports'
    serializer_class = UpdateSportsSerializer
    sports_service = SportsService

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            sport = self.get_sports_service().check_sport(serializer.data['id'])
            if sport:
                response = self.get_sports_service().update_sport(serializer.data)
                return Response(response['data'], status=response['status'])
        else:
            return Response('Sport ID not found.', status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_sports_service(self):
        return self.sports_service()


class ListSportsView(generics.GenericAPIView):
    """
    #List Sports
    Returns a list of sports.

    ---

    ##Supported Filters:

    * **name_regex (str)**: Search for sports with names satisfying a particular regex.

    * **is_active (int)**: Search for active/inactive sports. The value must be 0 or 1.


    ## Query Example:
        http://127.0.0.1:8000/sports/list?name_regex=abc&is_active=1 # filtering by name regex AND active events

    """
    name = 'list-sports'
    serializer_class = ListSportsSerializer
    sports_service = SportsService

    queryset = []

    def get(self, request, *args, **kwargs):
        response = self.get_sports_service().list_sports(request.query_params)
        return Response(response['data'], status=response['status'])

    def get_sports_service(self):
        return self.sports_service()

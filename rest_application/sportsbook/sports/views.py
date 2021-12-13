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

     * **name (str)**: Patch name.

     * **active (int)**: Patch active.

     """
    name = 'create-sports'
    serializer_class = CreateSportsSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = SportsService.create_sports(serializer.data)
            return Response(response['data'], status=response['status'])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            response = SportsService.update_sport(serializer.data)
            return Response(response['data'], status=response['status'])
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListSportsView(generics.GenericAPIView):
    """
    #List Sports
    Returns a list of sports.

    ---

    ##Supported Filters:

    * **name (str)**: Search for sports by matching name.

    * **name_regex (str)**: Search for sports with names satisfying a particular regex.

    * **active_events[lte] (int)**: Search for sports with a number of active events less than or equal the filter.

    * **active_events[gte] (int)**: Search for sports with a number of active events grater than or equal the filter.

    * **is_active (int)**: Search for active/inactive sports. The value must be 0 or 1.


    ## Query Example:
        http://127.0.0.1:8000/sports/list?name_regex=[abc]&active_events[gte]=1 # filtering by name regex AND one or more active events

    """
    name = 'list-sports'
    serializer_class = ListSportsSerializer

    def get(self, request, *args, **kwargs):
        response = SportsService.list_sports(request.query_params)
        return Response(response['data'], status=response['status'])

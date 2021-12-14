from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from events.services import EventsService
from selections.serializers import ListSelectionsSerializer, CreateSelectionsSerializer, UpdateSelectionsSerializer
from selections.services import SelectionsService
from sports.services import SportsService


class CreateSelectionsView(generics.GenericAPIView):
    """
     #Create Selections
     Create a event.

     ---

     ##Params:

     * **name (str)**: event name.

     * **active (int)**: event active.

     * **Type (str)**: event type.

     * **Sport (int)**: event id.

     * **Status (str)**: event status.

     * **Scheduled start (datetime)**: event scheduled start.

     """
    name = 'create-selections'
    serializer_class = CreateSelectionsSerializer
    event_service = EventsService
    selection_service = SelectionsService

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            event = self.event_service.fetch_event(serializer.data['event_id'])
            if event:
                response = self.selection_service.create_selections(serializer.data)
                return Response(response['data'], status=response['status'])
            else:
                return Response('Event ID not found.', status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UpdateSelectionsView(generics.GenericAPIView):
    """
    #Update Selections
    Update a event.

    ---

    ##Params:

     * **name (str)**: patch event name.

     * **active (int)**: patch event active.

     * **Type (str)**: patch event type.

     * **Sport (int)**: patch event id.

     * **Status (str)**: patch event status.

     * **Scheduled start (datetime)**: event scheduled start.

    """
    name = 'update-selections'
    serializer_class = UpdateSelectionsSerializer
    selection_service = SelectionsService

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            selection = self.selection_service.fetch_selection(serializer.data['id'])
            if selection:
                response = self.selection_service.update_selections(serializer.data)
                return Response(response['data'], status=response['status'])
            else:
                return Response('Selection ID not found.', status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListSelectionsView(generics.GenericAPIView):
    """
    #List Selections
    Returns a list of selections.

    ---

    ##Supported Filters:

    * **name_regex (str)**: Search for selections with names satisfying a particular regex.

    * **is_active (int)**: Search for active/inactive selections. The value must be 0 or 1.


    ## Query Example:
        http://127.0.0.1:8000/selections/list?name_regex=[abc]&active_selections[gte]=1 # filtering by name regex AND one or more active selections

    """
    name = 'list-selections'
    serializer_class = ListSelectionsSerializer
    event_service = SelectionsService
    queryset = []

    def get(self, request, *args, **kwargs):
        response = self.event_service.list_selections(request.query_params)
        return Response(response['data'], status=response['status'])

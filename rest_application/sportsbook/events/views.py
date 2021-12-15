from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from events.serializers import ListEventsSerializer, CreateEventsSerializer, UpdateEventsSerializer
from events.services import EventsService
from sports.services import SportsService


class CreateEventsView(generics.GenericAPIView):
    """
     #Create Events
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
    name = 'create-events'
    serializer_class = CreateEventsSerializer
    sports_service = SportsService
    event_service = EventsService

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            sport = self.get_sports_service().check_sport(serializer.data['sport_id'])
            if sport:
                response = self.get_event_service().create_events(serializer.data)
                return Response(response['data'], status=response['status'])
            else:
                return Response('Sport ID not found.', status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_sports_service(self):
        return self.sports_service()

    def get_event_service(self):
        return self.event_service()


class UpdateEventsView(generics.GenericAPIView):
    """
    #Update Events
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
    name = 'update-events'
    serializer_class = UpdateEventsSerializer
    event_service = EventsService

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            event = self.get_event_service().check_event(serializer.data['id'])
            if event:
                response = self.get_event_service().update_events(serializer.data)
                return Response(response['data'], status=response['status'])
            else:
                return Response('Event ID not found.', status=status.HTTP_404_NOT_FOUND)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_event_service(self):
        return self.event_service()


class ListEventsView(generics.GenericAPIView):
    """
    #List Events
    Returns a list of events.

    ---

    ##Supported Filters:

    * **name_regex (str)**: Search for events with names satisfying a particular regex.

    * **is_active (int)**: Search for active/inactive events. The value must be 0 or 1.


    ## Query Example:
        http://127.0.0.1:8000/events/list?name_regex=[abc]&active_events[gte]=1 # filtering by name regex AND one or more active events

    """
    name = 'list-events'
    serializer_class = ListEventsSerializer
    event_service = EventsService
    queryset = []

    def get(self, request, *args, **kwargs):
        response = self.get_event_service().list_events(request.query_params)
        return Response(response['data'], status=response['status'])

    def get_event_service(self):
        return self.event_service()
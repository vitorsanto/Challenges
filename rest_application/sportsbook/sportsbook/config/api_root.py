from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

from sports import urls as sports_urls
from events import urls as events_urls


class ApiRoot(generics.GenericAPIView):
    """
    Get the routes of available APIs
    """
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        urlpatterns = sports_urls.urlpatterns + events_urls.urlpatterns
        json_response = {}
        for url in urlpatterns:
            json_response.update({url.name: reverse(url.name, request=request)})

        return Response(json_response)

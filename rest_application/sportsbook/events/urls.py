from django.urls import path

from events.views import ListEventsView, CreateEventsView, UpdateEventsView

urlpatterns = [
    path('list', ListEventsView.as_view(), name=ListEventsView.name),
    path('create', CreateEventsView.as_view(), name=CreateEventsView.name),
    path('update', UpdateEventsView.as_view(), name=UpdateEventsView.name),
]

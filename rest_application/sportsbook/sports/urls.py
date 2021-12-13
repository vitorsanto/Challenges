from django.urls import path

from sports.views import ListSportsView, CreateSportsView, UpdateSportsView

urlpatterns = [
    path('list', ListSportsView.as_view(), name=ListSportsView.name),
    path('create', CreateSportsView.as_view(), name=CreateSportsView.name),
    path('update', UpdateSportsView.as_view(), name=UpdateSportsView.name),
]

from django.urls import path

from selections.views import ListSelectionsView, CreateSelectionsView, UpdateSelectionsView

urlpatterns = [
    path('list', ListSelectionsView.as_view(), name=ListSelectionsView.name),
    path('create', CreateSelectionsView.as_view(), name=CreateSelectionsView.name),
    path('update', UpdateSelectionsView.as_view(), name=UpdateSelectionsView.name),
]

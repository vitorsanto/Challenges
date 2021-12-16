import pytest
from django.http import QueryDict

from sports.serializers import CreateSportsSerializer, UpdateSportsSerializer


@pytest.fixture
def create_sports_serializer_fixture():
    return QueryDict('name=Soccer&active=true')


@pytest.fixture
def update_sports_serializer_fixture():
    return QueryDict('id=1&name=Golf&active=null')


def test_create_sports_serializer(create_sports_serializer_fixture):
    serializer = CreateSportsSerializer(data=create_sports_serializer_fixture)
    serializer.is_valid()
    assert serializer.data == {'name': 'Soccer', 'slug': 'soccer', 'active': True}


def test_update_sports_serializer(update_sports_serializer_fixture):
    serializer = UpdateSportsSerializer(data=update_sports_serializer_fixture)
    serializer.is_valid()
    assert serializer.data == {'id': 1, 'name': 'Golf', 'slug': 'golf'}

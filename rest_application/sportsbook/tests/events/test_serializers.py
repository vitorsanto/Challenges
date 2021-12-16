import pytest
from django.http import QueryDict

from events.serializers import CreateEventsSerializer, UpdateEventsSerializer


@pytest.fixture
def create_event_serializer_fixture():
    return QueryDict(
        'name=Game 3&active=true&type=preplay&sport_id=1&status=pending&scheduled_start=2021-12-16T14:53:00Z'
    )


@pytest.fixture
def create_event_serializer_error_fixture():
    return QueryDict('name=&active=true')


@pytest.fixture
def update_events_serializer_fixture():
    return QueryDict(
        'id=1&name=Game 3&active=&type=&sport_id=&status=&scheduled_start='
    )

@pytest.fixture
def update_events_serializer_error_fixture():
    return QueryDict('id=&name=Game 3')


def test_create_events_serializer(create_event_serializer_fixture):
    serializer = CreateEventsSerializer(data=create_event_serializer_fixture)
    serializer.is_valid()
    assert serializer.data == {
        'active': True,
        'name': 'Game 3',
        'scheduled_start': '2021-12-16T14:53:00Z',
        'slug': 'game-3',
        'sport_id': 1,
        'status': 'pending',
        'type': 'preplay'
    }


def test_create_events_serializer_error(create_event_serializer_error_fixture):
    serializer = CreateEventsSerializer(data=create_event_serializer_error_fixture)
    serializer.is_valid()
    assert str(serializer.errors['name'][0]) == 'This field may not be blank.'


def test_update_event_serializer(update_events_serializer_fixture):
    serializer = UpdateEventsSerializer(data=update_events_serializer_fixture)
    serializer.is_valid()
    assert serializer.data == {'id': 1, 'name': 'Game 3', 'slug': 'game-3'}


def test_update_event_serializer_error(update_events_serializer_error_fixture):
    serializer = UpdateEventsSerializer(data=update_events_serializer_error_fixture)
    serializer.is_valid()
    assert str(serializer.errors['id'][0]) == 'A valid integer is required.'

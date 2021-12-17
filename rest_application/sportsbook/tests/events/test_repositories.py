import pytest

from events.models import EventsModel
from events.repositories import EventsRepository
from sports.models import SportsModel


@pytest.fixture
def create_event_fixture():
    sport = SportsModel.objects.create(name='Soccer', slug='soccer', active=True)
    return {
        'name': 'Game 1',
        'slug': 'game-1',
        'active': True,
        'type': 'preplay',
        'sport_id': sport.id,
        'status': 'pending',
        'scheduled_start': '2021-12-16T14:53:00Z'
    }


@pytest.fixture
def update_event_fixture(create_event_fixture):
    attributes = ['id', 'name', 'slug', 'active']
    obj = EventsModel.objects.create(**create_event_fixture)
    return {attribute: getattr(obj, attribute) for attribute in attributes}


@pytest.fixture
def list_event_fixture():
    sport = SportsModel.objects.create(name='Soccer', slug='soccer', active=True)
    event_1 = {
        'name': 'Game 2',
        'slug': 'game-2',
        'active': False,
        'type': 'preplay',
        'sport_id': sport.id,
        'status': 'pending',
        'scheduled_start': '2021-12-16T14:53:00Z'
    }
    event_2 = {
        'name': 'Game 1',
        'slug': 'game-1',
        'active': True,
        'type': 'preplay',
        'sport_id': sport.id,
        'status': 'pending',
        'scheduled_start': '2021-12-16T14:53:00Z'
    }
    EventsModel.objects.create(**event_1)
    EventsModel.objects.create(**event_2)


@pytest.mark.django_db
def test_create_event(create_event_fixture):
    response = EventsRepository.create_event(create_event_fixture)
    assert response[1] == 'Game 1'
    assert response[2] == 'game-1'
    assert EventsModel.objects.count() == 1


@pytest.mark.django_db
def test_update_event(update_event_fixture):
    event = update_event_fixture
    event['name'] = 'Game 2'
    event['slug'] = 'game-2'
    response = EventsRepository.update_event(event)
    assert response[1] == 'Game 2'
    assert response[2] == 'game-2'
    assert EventsModel.objects.count() == 1


@pytest.mark.django_db
def test_list_events_filters(list_event_fixture):
    list_event_fixture
    events_list_1 = EventsRepository.list_events({'name_regex': '1'})
    events_list_2 = EventsRepository.list_events({'is_active': False})
    assert len(events_list_1) == 1
    assert events_list_1[0][2] == 'game-1'
    assert len(events_list_2) == 1
    assert events_list_2[0][2] == 'game-2'


@pytest.mark.django_db
def test_check_event(update_event_fixture):
    sport = EventsRepository.check_event(update_event_fixture['id'])
    assert sport[0] == update_event_fixture['id']


@pytest.mark.django_db
def test_events_active_from_sport(update_event_fixture):
    update_event_fixture
    selections = EventsRepository.events_active_from_sport(1)
    assert selections == 1

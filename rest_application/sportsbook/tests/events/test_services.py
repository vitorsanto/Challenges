from unittest import mock

import pytest

from events.services import EventsService


@pytest.fixture
def create_events_service_fixture():
    return {'name': 'Soccer', 'slug': 'soccer', 'active': True}


def mock_events_success(*args):
    return 'success'


def mock_events_error(*args):
    raise Exception('error')


@mock.patch('events.repositories.EventsRepository.create_event', mock_events_success)
def test_create_events_service_success(create_events_service_fixture):
    response = EventsService().create_events(create_events_service_fixture)
    assert response == {'data': 'success', 'status': 201}


@mock.patch('events.repositories.EventsRepository.create_event', mock_events_error)
def test_create_events_service_error(create_events_service_fixture):
    response = EventsService().create_events(create_events_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}


@mock.patch('events.repositories.EventsRepository.events_active_from_sport', mock_events_success)
@mock.patch('events.repositories.EventsRepository.update_event', mock_events_success)
def test_update_events_view_success(create_events_service_fixture):
    response = EventsService().update_events(create_events_service_fixture)
    assert response == {'data': 'success', 'status': 200}


@mock.patch('events.repositories.EventsRepository.update_event', mock_events_error)
def test_update_events_view_error(create_events_service_fixture):
    response = EventsService().update_events(create_events_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}


@mock.patch('events.repositories.EventsRepository.list_events', mock_events_success)
def test_list_events_view_success(create_events_service_fixture):
    response = EventsService().list_events(create_events_service_fixture)
    assert response == {'data': 'success', 'status': 200}


@mock.patch('events.repositories.EventsRepository.list_events', mock_events_error)
def test_list_events_view_error(create_events_service_fixture):
    response = EventsService().list_events(create_events_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}

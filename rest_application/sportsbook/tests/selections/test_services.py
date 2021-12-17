from unittest import mock

import pytest

from selections.services import SelectionsService


@pytest.fixture
def create_selections_service_fixture():
    return {'name': 'Selection', 'active': True}


def mock_selections_success(*args):
    return 'success'


def mock_selections_error(*args):
    raise Exception('error')


@mock.patch('selections.repositories.SelectionsRepository.create_selection', mock_selections_success)
def test_create_selections_service_success(create_selections_service_fixture):
    response = SelectionsService().create_selections(create_selections_service_fixture)
    assert response == {'data': 'success', 'status': 201}


@mock.patch('selections.repositories.SelectionsRepository.create_selection', mock_selections_error)
def test_create_selections_service_error(create_selections_service_fixture):
    response = SelectionsService().create_selections(create_selections_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}


@mock.patch('selections.repositories.SelectionsRepository.selections_active_from_event', mock_selections_success)
@mock.patch('selections.repositories.SelectionsRepository.update_selection', mock_selections_success)
def test_update_selections_view_success(create_selections_service_fixture):
    response = SelectionsService().update_selections(create_selections_service_fixture)
    assert response == {'data': 'success', 'status': 200}


@mock.patch('selections.repositories.SelectionsRepository.update_selection', mock_selections_error)
def test_update_selections_view_error(create_selections_service_fixture):
    response = SelectionsService().update_selections(create_selections_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}


@mock.patch('selections.repositories.SelectionsRepository.list_selections', mock_selections_success)
def test_list_events_view_success(create_selections_service_fixture):
    response = SelectionsService().list_selections(create_selections_service_fixture)
    assert response == {'data': 'success', 'status': 200}


@mock.patch('selections.repositories.SelectionsRepository.list_selections', mock_selections_error)
def test_list_events_view_error(create_selections_service_fixture):
    response = SelectionsService().list_selections(create_selections_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}

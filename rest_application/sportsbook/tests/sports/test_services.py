from unittest import mock

import pytest

from sports.services import SportsService


@pytest.fixture
def create_sports_service_fixture():
    return {'name': 'Soccer', 'slug': 'soccer', 'active': True}


def mock_sports_success(*args):
    return 'success'


def mock_sports_error(*args):
    raise Exception('error')


@mock.patch('sports.repositories.SportsRepository.create_sport', mock_sports_success)
def test_create_sports_service_success(create_sports_service_fixture):
    response = SportsService().create_sports(create_sports_service_fixture)
    assert response == {'data': 'success', 'status': 201}


@mock.patch('sports.repositories.SportsRepository.create_sport', mock_sports_error)
def test_create_sports_service_error(create_sports_service_fixture):
    response = SportsService().create_sports(create_sports_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}


@mock.patch('sports.repositories.SportsRepository.update_sport', mock_sports_success)
def test_update_sports_view_success(create_sports_service_fixture):
    response = SportsService().update_sport(create_sports_service_fixture)
    assert response == {'data': 'success', 'status': 200}


@mock.patch('sports.repositories.SportsRepository.update_sport', mock_sports_error)
def test_update_sports_view_error(create_sports_service_fixture):
    response = SportsService().update_sport(create_sports_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}


@mock.patch('sports.repositories.SportsRepository.list_sports', mock_sports_success)
def test_list_sports_view_success(create_sports_service_fixture):
    response = SportsService().list_sports(create_sports_service_fixture)
    assert response == {'data': 'success', 'status': 200}


@mock.patch('sports.repositories.SportsRepository.list_sports', mock_sports_error)
def test_list_sports_view_error(create_sports_service_fixture):
    response = SportsService().list_sports(create_sports_service_fixture)
    assert response == {'data': "Exception('error')", 'status': 500}

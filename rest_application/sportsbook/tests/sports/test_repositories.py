import pytest

from sports.models import SportsModel
from sports.repositories import SportsRepository


@pytest.fixture
def create_sport_fixture():
    return {'name': 'Soccer', 'slug': 'soccer', 'active': True}


@pytest.fixture
def update_sport_fixture(create_sport_fixture):
    attributes = ['id', 'name', 'slug', 'active']
    obj = SportsModel.objects.create(**create_sport_fixture)
    return {attribute: getattr(obj, attribute) for attribute in attributes}


@pytest.fixture
def list_user_fixture():
    sport_1 = {'name': 'Soccer', 'slug': 'soccer', 'active': True}
    sport_2 = {'name': 'Golf', 'slug': 'golf', 'active': False}
    SportsModel.objects.create(**sport_1)
    SportsModel.objects.create(**sport_2)


@pytest.mark.django_db
def test_create_sport(create_sport_fixture):
    response = SportsRepository.create_sport(create_sport_fixture)
    assert response[1] == 'Soccer'
    assert response[2] == 'soccer'
    assert SportsModel.objects.count() == 1


@pytest.mark.django_db
def test_update_sport(update_sport_fixture):
    sport = update_sport_fixture
    sport['name'] = 'Golf'
    sport['slug'] = 'golf'
    response = SportsRepository.update_sport(sport)
    assert response[1] == 'Golf'
    assert response[2] == 'golf'
    assert SportsModel.objects.count() == 1


@pytest.mark.django_db
def test_list_sport_filters(list_user_fixture):
    list_user_fixture
    sport_list_1 = SportsRepository.list_sports({'name_regex': 'Soc'})
    sport_list_2 = SportsRepository.list_sports({'is_active': False})
    assert len(sport_list_1) == 1
    assert sport_list_1[0][2] == 'soccer'
    assert len(sport_list_2) == 1
    assert sport_list_2[0][2] == 'golf'


@pytest.mark.django_db
def test_check_sport(update_sport_fixture):
    sport = SportsRepository.check_sport(update_sport_fixture['id'])
    assert sport[0] == update_sport_fixture['id']

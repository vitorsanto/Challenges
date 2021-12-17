import pytest

from selections.models import SelectionsModel
from selections.repositories import SelectionsRepository
from tests.factories import EventFactory, SportFactory


@pytest.fixture
@pytest.mark.django_db
def create_selection_fixture():
    event = EventFactory.create(sport_id=SportFactory.create().id)

    return {
        'name': 'Selection 1',
        'active': True,
        'price': 10,
        'event_id': event.id,
        'outcome': 'void',
    }


@pytest.fixture
def update_selection_fixture(create_selection_fixture):
    attributes = ['id', 'name', 'price', 'active']
    obj = SelectionsModel.objects.create(**create_selection_fixture)
    return {attribute: getattr(obj, attribute) for attribute in attributes}


@pytest.fixture
def list_selection_fixture():
    event = EventFactory.create(sport_id=SportFactory.create().id)

    selection_1 = {
        'name': 'Selection 1',
        'active': True,
        'price': 10,
        'event_id': event.id,
        'outcome': 'void',
    }

    selection_2 = {
        'name': 'Selection 2',
        'active': False,
        'price': 50,
        'event_id': event.id,
        'outcome': 'void',
    }

    SelectionsModel.objects.create(**selection_1)
    SelectionsModel.objects.create(**selection_2)


@pytest.mark.django_db
def test_create_event(create_selection_fixture):
    response = SelectionsRepository.create_selection(create_selection_fixture)
    assert response[1] == 'Selection 1'
    assert SelectionsModel.objects.count() == 1


@pytest.mark.django_db
def test_update_event(update_selection_fixture):
    selection = update_selection_fixture
    selection['name'] = 'New selection'
    selection['price'] = 20
    response = SelectionsRepository.update_selection(selection)
    assert response[1] == 'New selection'
    assert response[3] == 20
    assert SelectionsModel.objects.count() == 1


@pytest.mark.django_db
def test_list_selections_filters(list_selection_fixture):
    list_selection_fixture
    selections_list_1 = SelectionsRepository.list_selections({'name_regex': '1'})
    selections_list_2 = SelectionsRepository.list_selections({'is_active': False})
    assert len(selections_list_1) == 1
    assert selections_list_1[0][1] == 'Selection 1'
    assert len(selections_list_2) == 1
    assert selections_list_2[0][1] == 'Selection 2'


@pytest.mark.django_db
def test_check_selection(update_selection_fixture):
    selection = SelectionsRepository.check_selection(update_selection_fixture['id'])
    assert selection[0] == update_selection_fixture['id']


@pytest.mark.django_db
def test_selections_active_from_event(list_selection_fixture):
    list_selection_fixture
    selections = SelectionsRepository.selections_active_from_event(1)
    assert selections == 1

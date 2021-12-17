import pytest
from django.http import QueryDict

from selections.serializers import CreateSelectionsSerializer, UpdateSelectionsSerializer


@pytest.fixture
def create_selection_serializer_fixture():
    return QueryDict('name=Selection 1&active=true&price=10&event_id=1&outcome=void')


@pytest.fixture
def create_selection_serializer_error_fixture():
    return QueryDict('name=&active=true')


@pytest.fixture
def update_selections_serializer_fixture():
    return QueryDict('id=1&name=Updated Selection&active=&price=&event_id=&outcome=')


@pytest.fixture
def update_selections_serializer_error_fixture():
    return QueryDict('id=&name=Updated Selection')


def test_create_selections_serializer(create_selection_serializer_fixture):
    serializer = CreateSelectionsSerializer(data=create_selection_serializer_fixture)
    serializer.is_valid()
    assert serializer.data == {
        'active': True,
        'event_id': 1,
        'name': 'Selection 1',
        'outcome': 'void',
        'price': 10,
    }


def test_create_selections_serializer_error(create_selection_serializer_error_fixture):
    serializer = CreateSelectionsSerializer(data=create_selection_serializer_error_fixture)
    serializer.is_valid()
    assert str(serializer.errors['name'][0]) == 'This field may not be blank.'


def test_update_event_serializer(update_selections_serializer_fixture):
    serializer = UpdateSelectionsSerializer(data=update_selections_serializer_fixture)
    serializer.is_valid()
    assert serializer.data == {'id': 1, 'name': 'Updated Selection'}


def test_update_selection_serializer_error(update_selections_serializer_error_fixture):
    serializer = UpdateSelectionsSerializer(data=update_selections_serializer_error_fixture)
    serializer.is_valid()
    assert str(serializer.errors['id'][0]) == 'A valid integer is required.'

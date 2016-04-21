import pytest

from cc_dynamodb3.fields import (
    ValidationError,
    validate_no_empty_string_values,
)

from .factories.map_field_model import MapFieldModelFactory


def test_validate_raises_for_empty_strings_1():
    with pytest.raises(ValidationError):
        validate_no_empty_string_values({'first_name': ''})


def test_validate_raises_for_empty_strings_2():
    with pytest.raises(ValidationError) as exc_info:
        validate_no_empty_string_values({'nested': {'first_name': ''}})

    assert 'nested => first_name' in exc_info.value.message[0]


def test_map_field_model_validates():
    MapFieldModelFactory.create_table()
    model = MapFieldModelFactory(agency_subdomain='metzler')
    model.request_data = {'nested': {'data': {'first_name': ''}}}
    with pytest.raises(ValidationError):
        model.save()
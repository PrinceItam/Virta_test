# Simple API get request of Virta Stations with /stations/{id} end point
# Test platform Windows 10
# Python Version 3.10.0

import jsonschema
import requests
import pytest
from jsonschema import validate

stationSchema = {
    "id": "integer",
    "name": "string",
    "latitude": "number",
    "longitude": "number",
    "icon": "integer",
    "address": "string",
    "city": "string",
    "openHours": "string",
    "providers": "string",
    "pictures": "array[string]",
    "isV2G": "boolean",
    "eichrechtType": "string",
    "termsAndConditionsUrlActingEmp": "string",
    "termsLink": "string",

}

station_id = 233236
baseURL = f"https://api.virta.fi/v4/stations/{station_id}"


def get_station():
    return requests.get(url=baseURL)


@pytest.fixture
def response():
    return get_station()


def test_station_status_code(response):
    assert response.status_code == 200


def test_stations_resonse_limit(response):
    assert len(response.json()) == 23


def test_valid_station_id(response):
    data = response.json()
    assert data['id'] == station_id


def test_valid_object_type(response):
    data = response.json()
    assert type(data['name']) == str


def test_valid_json_body(response):
    try:
        validate(instance=response, schema=stationSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True


def test_response_body_has_form_data(response):
    data = response.json()
    assert data['operatorName'] == "Clever A/S"

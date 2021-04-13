import pytest
from rest_framework.test import APIClient
from rest_framework_api_key.models import APIKey

from tracker.models import Location


@pytest.fixture
def api_key():
    key = APIKey.objects.create(name="Test")
    api_key = APIKey.objects.assign_key(key)
    key.save()
    return api_key


@pytest.fixture
def api_client(api_key):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION=f"Api-Key {api_key}")
    return client


@pytest.fixture
def locations():
    for i in range(3):
        location = Location(latitude=i, longitude=i)
        for attr in ("name", "address_1", "address_2", "city", "state", "country"):
            setattr(location, attr, f"{attr} {i}")
        location.save()

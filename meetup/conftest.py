import pytest
from rest_framework.test import APIClient

from tracker.models import City, Country, GroupUrlname, Location, MeetupGroup


@pytest.fixture
def api_client(api_key):
    client = APIClient()
    return client


@pytest.fixture
def locations():
    country = Country(name="Brasil")
    country.save()
    city1 = City(name="Sao Paulo", country=country)
    city1.save()
    city2 = City(name="Florianopolis", country=country)
    city2.save()

    for i, city in enumerate((city1, city2)):
        location = Location(city=city, latitude=i, longitude=i)
        for attr in ("name", "address_1", "address_2"):
            setattr(location, attr, f"{attr} {i}")
        location.save()


@pytest.fixture
def location():
    country = Country(name="Brasil")
    country.save()
    city = City(name="Sao Paulo", country=country)
    city.save()
    i = 99
    location = Location(city=city, latitude=i, longitude=i)
    for attr in ("name", "address_1", "address_2"):
        setattr(location, attr, f"{attr} {i}")
    location.save()
    return location


@pytest.fixture
def group_urlname():
    urlname = GroupUrlname(urlname="Python Group")
    urlname.save()
    return urlname


@pytest.fixture
def groups(location):
    for i in range(3):
        urlname = GroupUrlname(urlname=f"Python Group {i}")
        urlname.save()
        group = MeetupGroup(member_count=10, location=location, urlname=urlname)
        for attr in ("name", "description", "status", "link", "photo_link"):
            setattr(group, attr, f"{attr} {i}")
        group.save()


@pytest.fixture
def data_regression_model(data_regression):
    """
    Deletes the ids in the serialized data to avoid problems with data regression.
    """

    class DataRegressionWihoutId:
        def check(serialized):
            def delete_id(s):
                if isinstance(s, list):
                    for e in s:
                        delete_id(e)
                elif isinstance(s, dict):
                    if "id" in s:
                        del s["id"]

                    for attr in s.keys():
                        delete_id(s[attr])

            delete_id(serialized)
            data_regression.check(serialized)

    return DataRegressionWihoutId

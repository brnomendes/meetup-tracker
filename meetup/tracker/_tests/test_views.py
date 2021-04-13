import json

import pytest


@pytest.mark.django_db
def test_locations_view(api_client, data_regression_model, locations):
    response = api_client.get("/locations/")
    assert response.status_code == 200

    content = json.loads(response.content)
    data_regression_model.check(content)


@pytest.mark.django_db
def test_groups_view(api_client, data_regression_model, groups):
    response = api_client.get("/groups/")
    assert response.status_code == 200

    content = json.loads(response.content)
    data_regression_model.check(content)

import json

import pytest


@pytest.mark.django_db
def test_distributors_view(api_client, data_regression, locations):
    response = api_client.get("/locations/")
    assert response.status_code == 200

    content = json.loads(response.content)
    for c in content:
        # Deletes the id in the serialized data to avoid problems with data regression.
        del c["id"]
    data_regression.check(content)

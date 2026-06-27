from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_get_activities_returns_activities_dict():
    response = client.get("/activities")

    assert response.status_code == 200
    data = response.json()
    # Should return the same keys as the in-memory activities
    assert set(data.keys()) == set(activities.keys())


def test_root_redirects_to_static_index():
    # Don't follow redirects so we can assert the Location header
    response = client.get("/", follow_redirects=False)

    assert response.status_code in (301, 302, 307, 308)
    assert response.headers.get("location") == "/static/index.html"


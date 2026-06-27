from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_signup_adds_email_to_activity():
    activity_name = "Programming Class"
    email = "new-student@mergington.edu"
    activity = activities[activity_name]
    original_participants = activity["participants"][:]

    try:
        response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

        assert response.status_code == 200
        assert email in activity["participants"]
        assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    finally:
        activity["participants"] = original_participants


def test_signup_already_signed_up_returns_400():
    activity_name = "Programming Class"
    email = "existing-student@mergington.edu"
    activity = activities[activity_name]
    original_participants = activity["participants"][:]

    try:
        # Ensure email is present
        if email not in activity["participants"]:
            activity["participants"].append(email)

        response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

        assert response.status_code == 400
        assert response.json()["detail"] == "Student already signed up for this activity"
    finally:
        activity["participants"] = original_participants


def test_signup_activity_not_found_returns_404():
    activity_name = "Nonexistent Club"
    email = "someone@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_signup_adds_email_to_activity():
    activity_name = "Programming Class"
    email = "new-student@mergington.edu"
    activity = activities[activity_name]
    original_participants = activity["participants"][:]

    try:
        response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

        assert response.status_code == 200
        assert email in activity["participants"]
        assert response.json()["message"] == f"Signed up {email} for {activity_name}"
    finally:
        activity["participants"] = original_participants


def test_signup_already_signed_up_returns_400():
    activity_name = "Programming Class"
    email = "existing-student@mergington.edu"
    activity = activities[activity_name]
    original_participants = activity["participants"][:]

    try:
        # Ensure email is present
        if email not in activity["participants"]:
            activity["participants"].append(email)

        response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

        assert response.status_code == 400
        assert response.json()["detail"] == "Student already signed up for this activity"
    finally:
        activity["participants"] = original_participants


def test_signup_activity_not_found_returns_404():
    activity_name = "Nonexistent Club"
    email = "someone@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

from fastapi.testclient import TestClient

from src.app import activities, app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    activity_name = "Chess Club"
    email = "test-student@mergington.edu"
    activity = activities[activity_name]
    original_participants = activity["participants"][:]

    try:
        activity["participants"].append(email)

        response = client.delete(
            f"/activities/{activity_name}/participants/{email}"
        )

        assert response.status_code == 200
        assert email not in activity["participants"]
        assert response.json()["message"] == f"Removed {email} from {activity_name}"
    finally:
        activity["participants"] = original_participants


from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_get_students():
    client = app.test_client()
    response = client.get("/students")
    assert response.status_code == 200


def test_add_student():
    client = app.test_client()

    response = client.post(
        "/students",
        json={
            "name": "Sheerssh",
            "course": "Cloud Technology"
        }
    )

    assert response.status_code == 201


def test_student_not_found():
    client = app.test_client()
    response = client.get("/students/999")

    assert response.status_code == 404


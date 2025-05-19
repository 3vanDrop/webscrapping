import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_get_posts_status():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200


def test_create_post():
    payload = {"title": "foo", "body": "bar", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    assert response.json()["title"] == "foo"


def test_user_id_in_post():
    response = requests.get(f"{BASE_URL}/posts/1")
    data = response.json()
    assert data["userId"] == 1
from app.app import apppipy

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hello, CI/CD"
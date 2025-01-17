import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.data == b"Hello, CI/CD Pipeline"
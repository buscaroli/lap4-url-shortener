from app import app
import pytest

@pytest.fixture
def api():
    api = app.test_client()
    return api

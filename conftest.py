import pytest
from rest_framework.test import APIClient


@pytest.fixture(scope="function")
def api_client() -> APIClient:
    api_client = APIClient()
    return api_client

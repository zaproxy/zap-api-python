import pytest

import requests_mock

from zapv2 import ZAPv2


@pytest.fixture
def zap():
    """
    All tests will be able to share the instance of client with the same settings."""
    yield ZAPv2(apikey='testapikey')

@pytest.fixture
def zap_strict():
    """
    All tests will be able to share the instance of client with the same settings."""
    yield ZAPv2(apikey='testapikey', validate_status_code=True)

@pytest.fixture(autouse=True)
def client_mock():
    """Fixture create a mock for urllib library."""
    with requests_mock.mock() as mock:
        yield mock

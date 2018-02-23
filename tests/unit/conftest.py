import pytest

import requests_mock

from zapv2 import ZAPv2


@pytest.yield_fixture
def zap():
    """
    All tests will be able to share the instance of client with the same settings."""
    yield ZAPv2(apikey='testapikey')

@pytest.yield_fixture
def zap_strict():
    """
    All tests will be able to share the instance of client with the same settings."""
    yield ZAPv2(apikey='testapikey', validate_status_code=True)

@pytest.yield_fixture(autouse=True)
def client_mock():
    """Fixture create a mock for urllib library."""
    with requests_mock.mock() as mock:
        yield mock

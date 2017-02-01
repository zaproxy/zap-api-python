from mock import patch
import pytest

from zapv2 import ZAPv2

@pytest.yield_fixture
def zap():
    """
    All tests will be able to share the instance of client with the same settings."""
    yield ZAPv2()


@pytest.yield_fixture
def urllib_mock():
    """Fixture create a mock for urllib library."""
    with patch('zapv2.urllib.urlopen') as urllib_mock:
        yield urllib_mock

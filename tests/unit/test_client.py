"""
Tests related to the main Zap Client class
"""
from mock import call

TEST_PROXIES = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080',
}


def test_urlopen_proxies(zap, urllib_mock):
    """Check if Zap client passes proxy to urllib call."""
    urllib_mock.return_value.read.return_value = 'contents'

    assert zap.urlopen() == 'contents'
    assert urllib_mock.mock_calls[0][2]['proxies'] == TEST_PROXIES


def test_request_response(zap, urllib_mock):
    """Request method should return a python object from parsed output"""
    urllib_mock.return_value.read.return_value = '{"testkey": "testvalue"}'

    assert zap._request('http://allizom.org', {'querykey': 'queryvalue'}) == {'testkey': 'testvalue'}
    assert urllib_mock.mock_calls == [
        call('http://allizom.org?querykey=queryvalue', proxies=TEST_PROXIES),
        call().read()
    ]


def test_request_other(zap, urllib_mock):
    """_request_other should simply return a retrieved content."""
    urllib_mock.return_value.read.return_value = '{"testkey": "testvalue"}'

    assert zap._request('http://allizom.org', {'querykey': 'queryvalue'}) == {'testkey': 'testvalue'}
    assert urllib_mock.mock_calls == [
        call('http://allizom.org?querykey=queryvalue', proxies=TEST_PROXIES),
        call().read()
    ]

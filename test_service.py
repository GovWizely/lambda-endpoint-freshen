import pytest
import vcr

from service import handler


@vcr.use_cassette()
def test_handler(monkeypatch):
    """Reads from the `test_handler` cassette and processes the request
    """
    monkeypatch.setenv("API_KEY", "mykey")
    event = dict(freshen_url="https://api.trade.gov/v1/some_endpoint/freshen.json?api_key=")
    resp = handler(event, None)
    assert resp is True


@vcr.use_cassette()
def test_handler_fails(monkeypatch):
    """Reads from the `test_handler_fails` cassette and processes the invalid request
    """
    monkeypatch.setenv("API_KEY", "badkey")
    event = dict(freshen_url="https://api.trade.gov/v1/some_endpoint/freshen.json?api_key=")
    resp = handler(event, None)
    assert resp is False


@vcr.use_cassette()
def test_handler_raises(monkeypatch):
    """Reads from the `test_handler_raises` cassette and processes the request that raises
    """
    monkeypatch.setenv("API_KEY", "mykey")
    event = dict(freshen_url="https://hostdoesnotexist.gov/v1/some_endpoint/freshen.json?api_key=")
    resp = handler(event, None)
    assert resp is False


def test_api_key_set(monkeypatch):
    """ Ensures exception raised if api key is not set
    """
    monkeypatch.delenv("API_KEY", raising=False)
    event = dict(freshen_url="doesn't matter")
    with pytest.raises(KeyError):
        handler(event, None)

from request.request import Request
import pytest

def test_id():
    r = Request()
    assert r.__hash__() != 0
    assert r._id == -1
    r._id = 1
    assert r._id == 1

def test_await():
    r = Request()
    r.await_resp(0.01)
    r.response_ready()

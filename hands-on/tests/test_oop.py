import pytest

from exercises.oop import ApiResponse, Connection, ManagedConnection, timed

# Every test in this file is tagged "oop" — run just this file with
# `pytest -m oop -v`.
pytestmark = pytest.mark.oop


def test_api_response_ok_true_below_400():
    assert ApiResponse(status_code=200, body={}).ok is True
    assert ApiResponse(status_code=201, body={}).ok is True


def test_api_response_ok_false_at_and_above_400():
    assert ApiResponse(status_code=400, body={}).ok is False
    assert ApiResponse(status_code=500, body={}).ok is False


def test_api_response_equality():
    # A plain @dataclass gets __eq__ for free — this only fails if the
    # ApiResponse decorator/fields were changed.
    assert ApiResponse(200, {"a": 1}) == ApiResponse(200, {"a": 1})


def test_managed_connection_closes_normally():
    holder = {}
    with ManagedConnection() as conn:
        holder["conn"] = conn
        assert isinstance(conn, Connection)
        assert conn.closed is False
    assert holder["conn"].closed is True


def test_managed_connection_closes_even_on_error():
    holder = {}
    with pytest.raises(ValueError):
        with ManagedConnection() as conn:
            holder["conn"] = conn
            raise ValueError("boom")
    assert holder["conn"].closed is True


def test_timed_prints_a_duration_and_preserves_result(capsys):
    @timed
    def add_slow(a, b):
        return a + b

    result = add_slow(2, 3)

    captured = capsys.readouterr()
    assert result == 5
    assert "add_slow" in captured.out

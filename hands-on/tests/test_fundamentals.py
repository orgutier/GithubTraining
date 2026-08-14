import pytest

from exercises.fundamentals import (
    DivisionByZeroTestError,
    add,
    celsius_to_fahrenheit,
    classify_status,
    retry,
    safe_divide,
    sum_even_numbers,
)

# Every test in this file is tagged "fundamentals" — run just this file with
# `pytest -m fundamentals -v`.
pytestmark = pytest.mark.fundamentals


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212


@pytest.mark.parametrize(
    "code,expected",
    [
        (200, "success"),
        (201, "success"),
        (299, "success"),
        (400, "client error"),
        (404, "client error"),
        (499, "client error"),
        (500, "server error"),
        (503, "server error"),
        (100, "unknown"),
        (999, "unknown"),
    ],
)
def test_classify_status(code, expected):
    assert classify_status(code) == expected


def test_sum_even_numbers():
    assert sum_even_numbers(10) == 2 + 4 + 6 + 8 + 10
    assert sum_even_numbers(1) == 0
    assert sum_even_numbers(2) == 2


def test_retry_returns_first_success():
    calls = {"n": 0}

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise ValueError("not ready yet")
        return "ok"

    assert retry(flaky, attempts=5) == "ok"
    assert calls["n"] == 3


def test_retry_forwards_arguments():
    def add_with_offset(a, b, offset=0):
        return a + b + offset

    assert retry(add_with_offset, 2, 3, attempts=1, offset=10) == 15


def test_retry_raises_after_exhausting_attempts():
    def always_fails():
        raise ValueError("nope")

    with pytest.raises(ValueError):
        retry(always_fails, attempts=2)


def test_safe_divide():
    assert safe_divide(10, 2) == 5


def test_safe_divide_by_zero_raises_custom_error():
    with pytest.raises(DivisionByZeroTestError):
        safe_divide(10, 0)

"""
Part 1 exercises — core language fundamentals.

Every function below is incomplete. Replace each `raise NotImplementedError`
with a real implementation. Run just this section of the suite with:

    pytest -m fundamentals -v
"""


def add(a, b):
    """Return the sum of a and b."""
    raise NotImplementedError("implement add")


def celsius_to_fahrenheit(c):
    """Convert a Celsius temperature to Fahrenheit: c * 9 / 5 + 32."""
    raise NotImplementedError("implement celsius_to_fahrenheit")


def classify_status(code):
    """
    Classify an HTTP status code into one of four buckets:
      - "success"      for 200-299
      - "client error"  for 400-499
      - "server error"  for 500-599
      - "unknown"       for anything else
    """
    raise NotImplementedError("implement classify_status")


def sum_even_numbers(n):
    """Return the sum of every even number from 1 to n, inclusive."""
    raise NotImplementedError("implement sum_even_numbers")


def retry(func, *args, attempts=3, **kwargs):
    """
    Call func(*args, **kwargs), retrying on any exception, up to `attempts`
    times total. Return the first successful result. If every attempt
    raises, let the final exception propagate.
    """
    raise NotImplementedError("implement retry")


class DivisionByZeroTestError(Exception):
    """Raised by safe_divide instead of letting ZeroDivisionError escape."""


def safe_divide(a, b):
    """
    Return a / b. If b is 0, catch the ZeroDivisionError and raise
    DivisionByZeroTestError instead, with a message that includes both
    a and b.
    """
    raise NotImplementedError("implement safe_divide")

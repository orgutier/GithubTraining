"""
Part 2 exercises — dataclasses, context managers, decorators.

Every incomplete piece below is marked with a TODO or a
`raise NotImplementedError`. Run just this section of the suite with:

    pytest -m oop -v
"""

import functools
from dataclasses import dataclass


@dataclass
class ApiResponse:
    """A minimal stand-in for a parsed API response."""

    status_code: int
    body: dict

    @property
    def ok(self) -> bool:
        """Return True when status_code is below 400, False otherwise."""
        raise NotImplementedError("implement ApiResponse.ok")


class Connection:
    """A stand-in for any external resource that needs to be closed."""

    def __init__(self):
        self.closed = False

    def close(self):
        self.closed = True


class ManagedConnection:
    """
    A context manager that opens a Connection on __enter__ and guarantees
    it's closed on __exit__ — even if the code inside the `with` block
    raises an exception.
    """

    def __enter__(self):
        # TODO: create a Connection, store it on self, and return it.
        raise NotImplementedError("implement ManagedConnection.__enter__")

    def __exit__(self, exc_type, exc, tb):
        # TODO: close the connection. Do not suppress the exception —
        # returning a truthy value here would swallow it.
        raise NotImplementedError("implement ManagedConnection.__exit__")


def timed(func):
    """
    A decorator that, when the wrapped function is called, prints a message
    like "<function name> took <seconds>s" to stdout, then returns the
    wrapped function's result unchanged.
    """
    # TODO: write an inner `wrapper(*args, **kwargs)` that times the call
    # to func, prints the duration, and returns func's result. Don't forget
    # @functools.wraps(func) on the wrapper.
    raise NotImplementedError("implement timed")

"""
Part 5 exercises — the requests library.

Both functions below call a fake API at `base_url`. The test suite mocks
the network with the `responses` library, so no real HTTP calls are made —
but the code you write here must call `requests` for real, in the shape a
production client would.

Run just this section of the suite with:

    pytest -m apis -v
"""

import requests


def get_active_users(base_url):
    """
    GET {base_url}/users with a query parameter active=true, using a
    timeout. Raise on any 4xx/5xx response. Return the parsed JSON list
    of users.
    """
    raise NotImplementedError("implement get_active_users")


def create_user(base_url, payload):
    """
    POST payload (a dict) as JSON to {base_url}/users, using a timeout.
    Raise on any 4xx/5xx response. Return the parsed JSON dict describing
    the created user.
    """
    raise NotImplementedError("implement create_user")

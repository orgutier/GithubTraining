import pytest
import requests
import responses

from exercises.apis import create_user, get_active_users

# Every test in this file is tagged "apis" — run just this file with
# `pytest -m apis -v`.
pytestmark = pytest.mark.apis


@responses.activate
def test_get_active_users_returns_parsed_json(base_url):
    responses.add(
        responses.GET,
        f"{base_url}/users",
        json=[{"id": 1, "name": "Ada", "active": True}],
        status=200,
    )

    users = get_active_users(base_url)

    assert users == [{"id": 1, "name": "Ada", "active": True}]


@responses.activate
def test_get_active_users_sends_active_param(base_url):
    responses.add(
        responses.GET,
        f"{base_url}/users",
        json=[],
        status=200,
    )

    get_active_users(base_url)

    assert len(responses.calls) == 1
    assert responses.calls[0].request.params.get("active") in ("True", "true")


@responses.activate
def test_get_active_users_raises_on_server_error(base_url):
    responses.add(responses.GET, f"{base_url}/users", status=500)

    with pytest.raises(requests.exceptions.HTTPError):
        get_active_users(base_url)


@responses.activate
def test_create_user_returns_parsed_json(base_url):
    responses.add(
        responses.POST,
        f"{base_url}/users",
        json={"id": 2, "name": "Grace", "role": "engineer"},
        status=201,
    )

    user = create_user(base_url, {"name": "Grace", "role": "engineer"})

    assert user["name"] == "Grace"


@responses.activate
def test_create_user_sends_json_body(base_url):
    responses.add(
        responses.POST,
        f"{base_url}/users",
        json={"id": 3, "name": "Priya"},
        status=201,
    )

    create_user(base_url, {"name": "Priya"})

    assert responses.calls[0].request.body is not None
    assert b"Priya" in responses.calls[0].request.body


@responses.activate
def test_create_user_raises_on_client_error(base_url):
    responses.add(responses.POST, f"{base_url}/users", status=400)

    with pytest.raises(requests.exceptions.HTTPError):
        create_user(base_url, {"name": ""})

import pytest


@pytest.fixture
def base_url():
    """Shared fake API base URL used by every test in tests/test_apis.py."""
    return "https://api.example.com"

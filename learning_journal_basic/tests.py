import pytest
from pyramid import testing


@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import list_view
    response = list_view(req)
    some_html = 'Day 11 - Heroku seemed easier last time'
    assert some_html in str(response)

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


def test_detail_page_renders_file_data(req):
    """My home page view returns some data."""
    from .views import detail
    response = testapp.get('/', status=200)
    
    some_html = 'Julien'
    assert some_html in str(response)


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)

def test_layout_root(testapp):
    """Test that the contents of the root page contains <article>."""
    response = testapp.get('/', status=200)
    html = response.html
    assert 'Created in the Code Fellows 401 Python Program' in html.find("footer").text

def test_root_contents(testapp):
    """Test that the contents of the root page contains as many <article> tags as journal entries."""
    from .views import ENTRIES

    response = testapp.get('/', status=200)
    html = response.html
    assert len(ENTRIES) == len(html.findAll("article"))
import pytest
from pyramid import testing
from .views import ENTRIES


@pytest.fixture
def req():
    the_request = testing.DummyRequest()
    return the_request


def test_home_page_renders_file_data(req):
    """My home page view returns some appropriate data."""
    from .views import list_view
    response = list_view(req)
    some_html = 'Day 11 - Heroku seemed easier last time'
    assert some_html in str(response)


def test_detail_page_renders_file_data(req):
    """My detail page view returns some appropriate data."""
    from .views import detail
    req.matchdict['id'] = '10'
    response = detail(req)
    some_html = 'learned stuff again'
    assert some_html in str(response)


def test_edit_page_renders_file_data(req):
    """My edit page view returns data from the approriate post."""
    from .views import list_view
    req.matchdict['id'] = '12'
    response = list_view(req)
    some_html = "Big news today was finalizing projects and getting our groups.  I'm pretty excited to see how all of the projects pan out."
    assert some_html in str(response)


# ------- Functional Tests -------


@pytest.fixture()
def testapp():
    """Create an instance of our app for testing."""
    from learning_journal_basic import main
    app = main({})
    from webtest import TestApp
    return TestApp(app)


def test_home_root(testapp):
    """Test that the home page has appropriate html text."""
    response = testapp.get('/', status=200)
    html = response.html
    assert "Day 11 - Heroku seemed easier last time" in html.text


def test_home_root_num_of_posts(testapp):
    """Test that the home page has appropriate number of posts."""
    response = testapp.get('/', status=200)
    html = response.html
    postnum = len(html.findAll('h3'))
    assert postnum == len(ENTRIES)


def test_detail_root(testapp):
    """Test that the contents of the detail page contains proper body text."""
    response = testapp.get('/journal/12', status=200)
    html = response.html
    assert "Big news today was finalizing projects" in html.text


def test_create_page(testapp):
    """Test that the create page has some unique html text."""
    response = testapp.get('/journal/new-entry', status=200)
    html = response.html
    assert "New Post:" in html.text


def test_edit_page_11(testapp):
    """Test that the edit page has some html text appropriate to the post."""
    response = testapp.get('/journal/11/edit-entry', status=200)
    html = response.html
    assert 'Heroku seemed easier last time' in html.text


def test_edit_page_10(testapp):
    """Test that the contents of edit page has appropriate text."""
    response = testapp.get('/journal/10/edit-entry', status=200)
    html = response.html
    assert 'Start Bootstrap' in html.text


def test_edit_page_neg_10(testapp):
    """Test that the contents of edit page does not have inappropriate text."""
    response = testapp.get('/journal/10/edit-entry', status=200)
    html = response.html
    assert 'Starting out Final Projects' not in html.text


def test_layout_404_root(testapp):
    """Test that the contents of the root page contains <article>."""
    response = testapp.get('/squireels', status=404)

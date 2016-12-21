# from pyramid.response import Response
from pyramid.view import view_config
import io
import os

THIS_DIR = os.path.dirname(__file__)


ENTRIES = {
    '11': {"title":"Day 11 - Heroku seemed easier last time",
     "id": 11,
     "date": "December 19, 2016 AD",
     "body": "My main accomplishment today was debugging Heroku. My initial push (and my second attempt) failed, but I was able to read the errror messages and figure out what was going on.  I moved some files around and was able to make it work.  Generally, one of the things I've learned the most about in this class is reading error messages and figuring out how to fix them. Besides that, we presented ideas today.  Despite almost nobody having any ideas 5 minutes before the meeting, there were A LOT of great ideas.  I think people are thinking big.  Would be excited to work on a number of them. Data Structures are starting to feel more natural.  The Deque wasnt too tough today.  I've heard the heap is a little more exciting.  We'll see what that brings tomorrow."},
    '10': {"title": "Start Bootstrap",
     "id": 10,
     "date": "today",
     "body": "learned stuff again"},
    '9': {"title": "post3",
     "id": 9,
     "date": "today",
     "body": "learned stuff again again"},
}


@view_config(route_name="home", renderer="templates/posts.jinja2")
def list_view(request):
    """View for the blog with all of the posts listed."""
    # imported_file = open(os.path.join(THIS_DIR, 'static', 'index.html')).read()
    # # return Response(imported_file)
    # return imported_file
    return {"ENTRIES": ENTRIES}


@view_config(route_name="edit", renderer="string")
def update(request):
    """View """
    imported_file = open(os.path.join(THIS_DIR, 'static', 'edit_article.html')).read()
    # return Response(imported_file)
    return imported_file


@view_config(route_name="blog", renderer="string")
def detail(request):
    imported_file = open(os.path.join(THIS_DIR, 'static', 'article.html')).read()
    return Response(imported_file)


@view_config(route_name="new", renderer="string")
def create(request):
    imported_file = open(os.path.join(THIS_DIR, 'static', 'new_article.html')).read()
    return Response(imported_file)


# def includeme(config):
#     config.add_view(list_view, route_name='home')
#     config.add_view(detail, route_name='blog')
#     config.add_view(create, route_name='new')
#     config.add_view(update, route_name='edit')

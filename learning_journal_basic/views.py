# from pyramid.response import Response
from pyramid.view import view_config
# import io
import os
from pyramid.httpexceptions import HTTPFound


THIS_DIR = os.path.dirname(__file__)


ENTRIES = [
    {"title": "Starting out Final Projects",
     "id": '12',
     "date": "December 20, 2016",
     "body": "Big news today was finalizing projects and getting our groups.  I'm pretty excited to see how all of the projects pan out.  I think they're all pretty ambitious.  Lecture this morning was challenging.  A lot of new material that seemed daunting.  The bin heap was hard.  I think Patrick and I benefited some lots of diagramming.  I think that might be the key to these daa structures.  Also reading the instructions carefully. I tend to make mistakes there.  The pyramid stuff today felt satisfying once we got it working.  It feels like a real website... almost.      Part 2:  I just finished a debugging effort, which led me through the pyramid debugger toolbar, into the filter function (and its diferences in py2 and py3) some other steps.  None of these solutions fixed my problem, but I learned a lot about other things."},
    {"title": "Day 11 - Heroku seemed easier last time",
     "id": '11',
     "date": "December 19, 2016",
     "body": "My main accomplishment today was debugging Heroku. My initial push (and my second attempt) failed, but I was able to read the errror messages and figure out what was going on.  I moved some files around and was able to make it work.  Generally, one of the things I've learned the most about in this class is reading error messages and figuring out how to fix them. Besides that, we presented ideas today.  Despite almost nobody having any ideas 5 minutes before the meeting, there were A LOT of great ideas.  I think people are thinking big.  Would be excited to work on a number of them. Data Structures are starting to feel more natural.  The Deque wasnt too tough today.  I've heard the heap is a little more exciting.  We'll see what that brings tomorrow."},
    {"title": "Start Bootstrap",
     "id": '10',
     "date": "today",
     "body": "learned stuff again"},
    {"title": "post3",
     "id": '9',
     "date": "today",
     "body": "learned stuff again again"},
]


@view_config(route_name="home", renderer="templates/posts.jinja2")
def list_view(request):
    """View for the blog with all of the posts listed."""
    return {"ENTRIES": ENTRIES}


@view_config(route_name="edit", renderer="templates/update_post_template.jinja2")
def update(request):
    """View to edit a specific blog post."""
    the_id = request.matchdict["id"]
    entry = [item for item in ENTRIES if item['id'] == the_id][0]
    return {"entry": entry}


@view_config(route_name="blog", renderer="templates/detail.jinja2")
def detail(request):
    """View to show only a specific post with its body."""
    the_id = request.matchdict["id"]
    entry = [item for item in ENTRIES if item['id'] == the_id][0]
    return {"entry": entry}


@view_config(route_name="new", renderer="templates/new_post_template.jinja2")
def create(request):
    """View to create a new post."""
    return {}
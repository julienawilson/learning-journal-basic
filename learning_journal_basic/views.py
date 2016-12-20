from pyramid.response import Response


import os

THIS_DIR = os.path.dirname(__file__)


def list_view(request):
    """View for the blog with all of the posts listed."""
    imported_file = open(os.path.join(THIS_DIR, 'static', 'index.html')).read()
    return Response(imported_file)


def update(request):
    """View """
    imported_file = open(os.path.join(THIS_DIR, 'static', 'edit_article.html')).read()
    return Response(imported_file)


def detail(request):
    imported_file = open(os.path.join(THIS_DIR, 'static', 'article.html')).read()
    return Response(imported_file)


def create(request):
    imported_file = open(os.path.join(THIS_DIR, 'static', 'new_article.html')).read()
    return Response(imported_file)


def includeme(config):
    config.add_view(list_view, route_name='home')
    config.add_view(detail, route_name='blog')
    config.add_view(create, route_name='new')
    config.add_view(update, route_name='edit')

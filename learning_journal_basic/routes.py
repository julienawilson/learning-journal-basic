

def includeme(config):
    """ This function adds routes to Pyramid's Configurator """
    config.add_static_view(name='static', path='learning-journal-basic:static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('blog', '/journal/{id:\d+}')
    config.add_route('new', '/journal/new-entry')
    config.add_route('edit', '/journal/{id:\d+}/edit-entry')

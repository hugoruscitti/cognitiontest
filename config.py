import os

class Configuration(object):
    DATABASE = {
        'name': 'example.db',
        'engine': 'peewee.SqliteDatabase',
        'check_same_thread': False,
    }
    DEBUG = True
    SECRET_KEY = 'shhhh'

if 'HEROKU_POSTGRESQL_TEAL_URL' in os.environ:
    import urlparse

    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ['HEROKU_POSTGRESQL_TEAL_URL'])
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'password': url.password,
        'host': url.hostname,
        'port': url.port,
    }

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
    print "Detectando base de datos HEROKU POSTGRE"
    import urlparse

    urlparse.uses_netloc.append('postgres')
    url = urlparse.urlparse(os.environ['HEROKU_POSTGRESQL_TEAL_URL'])
    DATABASE = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': url.path[1:],
        'password': url.password,
        'user': url.username,
        'host': url.hostname,
        'port': url.port,
    }
    Configuration.DATABASE = DATABASE
else:
    print "Usando base de datos sqlite"

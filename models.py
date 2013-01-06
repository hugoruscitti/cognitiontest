from hashlib import md5
import datetime

from flask_peewee.auth import BaseUser
from peewee import *

from app import db


class User(db.Model, BaseUser):
    nombre = CharField()
    ingresado = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return self.nombre

class Relationship(db.Model):
    from_user = ForeignKeyField(User, related_name='relationships')
    to_user = ForeignKeyField(User, related_name='related_to')
    active = BooleanField(default=True)
    admin = BooleanField(default=False)

    def __unicode__(self):
        return 'Relationship from %s to %s' % (self.from_user, self.to_user)

    def following(self):
        return User.select().join(
            Relationship, on=Relationship.to_user
        ).where(Relationship.from_user==self).order_by(User.username)

    def followers(self):
        return User.select().join(
            Relationship, on=Relationship.from_user
        ).where(Relationship.to_user==self).order_by(User.username)

    def is_following(self, user):
        return Relationship.select().where(
            Relationship.from_user==self,
            Relationship.to_user==user
        ).exists()

    def gravatar_url(self, size=80):
        return 'http://www.gravatar.com/avatar/%s?d=identicon&s=%d' % \
            (md5(self.email.strip().lower().encode('utf-8')).hexdigest(), size)




class Message(db.Model):
    user = ForeignKeyField(User)
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)

    def __unicode__(self):
        return '%s: %s' % (self.user, self.content)


class Note(db.Model):
    user = ForeignKeyField(User)
    message = TextField()
    status = IntegerField(choices=((1, 'live'), (2, 'deleted')), null=True)
    created_date = DateTimeField(default=datetime.datetime.now)

def create_table(a_class):
    print "Creando la tabla:", a_class.__name__
    a_class.drop_table(True)
    a_class.create_table()

def create_tables():
    create_table(User)
    create_table(Relationship)
    create_table(Message)
    create_table(Note)

def create_fixture():
    user = User(nombre="Hugo")
    user.save()
    print "Creando usuario de prueba:", user

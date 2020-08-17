from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('locations.sqlite')

class Location(Model):
    city = CharField()
    latitude = CharField()
    longitude = CharField()
    image = CharField()
    description = CharField()
    visited = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Location], safe=True)
    DATABASE.close()
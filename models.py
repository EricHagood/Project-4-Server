from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('locations.sqlite')

class Location(Model):
    name = CharField()
    coordinates = CharField()
    image = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Location], safe=True)
    DATABASE.close()
from peewee import *
import datetime
from flask_login import UserMixin

DATABASE = SqliteDatabase('locations.sqlite')

class Location(Model):
    name = CharField()
    cooedinates = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Locations], safe=True)
    DATABASE.close()
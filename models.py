from peewee import *
import datetime
from flask_login import UserMixin
from playhouse.db_url import connect
import os

if 'ON_HEROKU' in os.environ:
    DATABASE = connect(os.environ.get('DATABASE_URL'))

else: 
    DATABASE = SqliteDatabase('location.sqlite')

class Location(Model):
    city = CharField()
    latitude = CharField()
    longitude = CharField()
    image = CharField(null = True)
    description = CharField()
    visited = CharField()
    
    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    print('f')
    DATABASE.create_tables([Location], safe=True)
    print("TABLE created")
    # seed() 
    DATABASE.close()

def seed():
    row = {
        'city': 'test',
        'latitude': '12.248754',
        'longitude': '78.685434',
        'image': '5asdjhfjakg78a0dyfhaeoew5uyhj',
        'description': 'N/A',
        'visited': 'false'
    }
    Location.insert(row).execute()
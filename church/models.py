
 

from mongoengine import *
import datetime

class Churches(Document):
  name = StringField()
  city = StringField()
  pastor = StringField()
  created_at = DateTimeField(default=datetime.datetime.utcnow)
  updated_at = DateTimeField(default=datetime.datetime.utcnow)

  meta = {
    'ordering': ['name']
  }

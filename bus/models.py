from mongoengine import *
import datetime

class Buses(Document):
  description = StringField()
  number_of_seats = IntField()
  value = FloatField()
  departure_date = DateField()
  return_date = DateField()
  created_at = DateTimeField(default=datetime.datetime.utcnow)
  updated_at = DateTimeField(default=datetime.datetime.utcnow)

  meta = {
    'ordering': ['-departure_date']
  }
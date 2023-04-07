from mongoengine import *
import datetime

class Members(Document):
  name = StringField()
  is_active = BooleanField()
  birth_date = DateField()
  cpf = StringField()
  phone = StringField()
  blood_type = StringField()
  gender = StringField()
  created_at = DateTimeField(default=datetime.datetime.utcnow)
  updated_at = DateTimeField(default=datetime.datetime.utcnow)

  meta = {
    'ordering': ['name']
  }
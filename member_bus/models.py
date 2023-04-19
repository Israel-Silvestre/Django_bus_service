from mongoengine import *
from bus.models import Buses
from member.models import Members
import datetime

class MemberBuses(Document):
  bus_id = ReferenceField(Buses, required=True)
  member_id = ReferenceField(Members, required=True)
  created_at = DateTimeField(default=datetime.datetime.utcnow)
  updated_at = DateTimeField(default=datetime.datetime.utcnow)

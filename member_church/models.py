from mongoengine import *
from church.models import Churches
from member.models import Members
import datetime

class MemberChurches(Document):
  church_id = ReferenceField(Churches, required=True)
  member_id = ReferenceField(Members, required=True)
  is_active = BooleanField(default=True)
  is_current = BooleanField(default=True)
  created_at = DateTimeField(default=datetime.datetime.utcnow)
  updated_at = DateTimeField(default=datetime.datetime.utcnow)

from rest_framework_mongoengine.serializers import DocumentSerializer
from member.models import Members

class MemberSerializer(DocumentSerializer):
  class Meta:
    model = Members
    fields = ('id', 'name', 'birth_date', 'cpf', 'phone', 'blood_type', 'gender')
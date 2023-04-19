from church.models import Churches
from member.models import Members
from member_church.models import MemberChurches
from church.serializers import ChurchSerializer
from member.serializers import MemberSerializer
from member_church.serializers import MemberChurchSerializer
from rest_framework_mongoengine import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from operator import itemgetter

class ChurchList(generics.ListAPIView):
  queryset = Churches.objects.all()
  serializer_class = ChurchSerializer

@api_view(['GET'])
def get_members(request, id, format=None):
  try:
    church = Churches.objects.get(pk=id)
  except Churches.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    mc = MemberChurches.objects(church_id=church.id)
    mc_serializer = MemberChurchSerializer(mc, many=True)
    
    members = []
    for mc_relationship in mc_serializer.data:
      member = Members.objects.get(pk=mc_relationship['member_id'])
      member_serializer = MemberSerializer(member)
      members.insert(0, member_serializer.data)
    members = sorted(members, key=itemgetter('name')) 

    return Response(members, status=status.HTTP_200_OK)
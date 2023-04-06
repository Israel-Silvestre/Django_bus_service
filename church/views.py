from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from church.models import *
from church.serializers import ChurchSerializer

@api_view(['GET'])
def church_index(request, format=None):
  churches = Churches.objects.all()
  serializer = ChurchSerializer(churches, many=True)
  output = {
    'message': 'Igrejas Listadas com Sucesso',
    'data': serializer.data
  }
  return Response(output, status=status.HTTP_200_OK)
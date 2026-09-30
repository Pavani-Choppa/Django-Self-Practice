from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,AllowAny

# public view
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({'message': 'This is a public view.'})

# private view
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({'message': 'This is a private view.'})

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import *
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#authentications

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.decorators import api_view, permission_classes
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
class EmployeeListCreate(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username, password=password)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def fetchAllEmployee(request):
    p=[permissions.IsAuthenticated]
    querySet=Employee.objects.all()
    serializer=EmployeeSerializer(querySet,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
@swagger_auto_schema(request_body=EmployeeSerializer, responses={201: EmployeeSerializer})
def AddEmployee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def UpdateEmployee(request,pk):
    try:
        item = Employee.objects.get(pk=pk)
        serializer = EmployeeSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response("Updated Successfully",status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
  
    
    

@api_view(['DELETE'])
def delete( request, pk, format=None):
    try:
        item = Employee.objects.get(pk=pk)
        item.delete()
        return Response("deleted Successfully",status=status.HTTP_200_OK)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
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

@api_view(['GET'])
def fetchAllEmployee(request):
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
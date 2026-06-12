from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Test
from .serializers import TestSerializer
from django.shortcuts import get_object_or_404


# CREATE + LIST
class TestListCreateView(APIView):
    
    
    def get(self, request):
        tests = Test.objects.all();
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data);
    
    
    def post(self , request):
        serializer = TestSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST )
        
        


# RETRIEVE + UPDATE + DELETE

class TestDetailView(APIView):
    def get_object(self , pk):
        return get_object_or_404(Test, pk=pk)
    
    
    
    def get(self , request , pk):
        test = self.get_object(pk)
        serializer = TestSerializer(test)
        return Response(serializer.data)
    
    
    def put(self , request , pk):
        test = self.get_object(pk)
        serializer = TestSerializer(test , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self, request , pk):
        test = self.get_object(pk)
        serializer = TestSerializer(test, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self , request, pk):
        test = self.get_object(pk)
        test.delete()
        return Response(
            {"message": "Deleted Successfully "},
            status=status.HTTP_204_NO_CONTENT
        )
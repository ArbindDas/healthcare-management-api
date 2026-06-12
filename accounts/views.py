from django.shortcuts import render
from rest_framework.permissions import AllowAny
# Create your views here.
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
# REGISTER USER
class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        
        serializer = UserSerializer(data=request.data)
        
        
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message": "User created successfully",
                    "user": UserSerializer(user).data
                    
                    
                }, status=status.HTTP_201_CREATED
            )
        else:
            return Response(serializer.errros , status=status.HTTP_400_BAD_REQUEST)



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Profile

from .serializers import ProfileSerializer

class MeView(APIView):
    
    permission_classes = [IsAuthenticated]
    def get(self , request):
        
        profile, created = Profile.objects.get_or_create(user=request.user)
        serializer= ProfileSerializer(profile)
        return Response(serializer.data)
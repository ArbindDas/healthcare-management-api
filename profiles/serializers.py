from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source="user.full_name", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)
    
    class Meta:
        model = Profile
        fields = [
            "full_name",
            "email",
            "phone",
            "address",
            "gender",
            "birthday"
        ]
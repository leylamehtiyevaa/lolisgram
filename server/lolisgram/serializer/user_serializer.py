from rest_framework import serializers
from lolisgram.models.user_model import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = CustomUser
        fields = (
            'email', 
            'username', 
            'password', 
            'first_name', 
            'last_name', 
            'phone_number', 
            'profile_picture',
            'bio',
            'followers',
            'following',
            )

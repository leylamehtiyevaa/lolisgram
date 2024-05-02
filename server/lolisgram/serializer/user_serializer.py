from rest_framework import serializers
from lolisgram.models.user_model import User

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = User
        fields = '__all__'

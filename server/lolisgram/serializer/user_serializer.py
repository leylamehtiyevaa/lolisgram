from rest_framework import serializers
from lolisgram.models.user_model import CustomUser

class UserSerializer(serializers.ModelSerializer):
    """
    User serializer
    """
    class Meta:
        model = CustomUser
        fields = '__all__'

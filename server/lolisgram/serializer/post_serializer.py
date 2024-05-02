from rest_framework import serializers
from lolisgram.models.posts_model import Post

class PostSerializer(serializers.ModelSerializer):  
    """
    Post serializer
    """
    class Meta:
        model = Post
        fields = '__all__'
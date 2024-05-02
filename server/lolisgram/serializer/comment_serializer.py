from rest_framework import serializers
from lolisgram.models.comments_model import Comment

class CommentSerializer(serializers.ModelSerializer):
    """
    Comment serializer
    """
    class Meta:
        model = Comment
        fields = '__all__'
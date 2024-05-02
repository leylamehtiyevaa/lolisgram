from rest_framework import viewsets, permissions
from rest_framework.response import Response
from lolisgram.serializer.comment_serializer import CommentSerializer
from lolisgram.models.comments_model import Comment
from rest_framework import status

class CommentViewSet(viewsets.ModelViewSet):
    """
    Comment viewset
    """
    queryset = Comment.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CommentSerializer
    def create(self, request, *args, **kwargs):
        """
        Create a new comment
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        """
        Update a comment
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        """
        Delete a comment
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
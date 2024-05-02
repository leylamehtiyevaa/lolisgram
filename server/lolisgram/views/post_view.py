from rest_framework import viewsets, permissions
from rest_framework.response import Response
from lolisgram.serializer.post_serializer import PostSerializer
from lolisgram.models.posts_model import Post
from rest_framework import status

class PostViewSet(viewsets.ModelViewSet):
    """
    Post viewset
    """
    queryset = Post.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PostSerializer
    def create(self, request, *args, **kwargs):
        """
        Create a new post
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        """
        Update a post
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        """
        Delete a post
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
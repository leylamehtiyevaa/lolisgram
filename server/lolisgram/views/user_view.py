from rest_framework import viewsets, permissions
from rest_framework.response import Response
from lolisgram.serializer.user_serializer import UserSerializer
from lolisgram.models.user_model import User
from rest_framework import status

class UserViewSet(viewsets.ModelViewSet):
    """
    User viewset
    """
    queryset = User.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer
    def create(self, request, *args, **kwargs):
        """
        Create a new user
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
    def update(self, request, *args, **kwargs):
        """
        Update a user
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    def destroy(self, request, *args, **kwargs):
        """
        Delete a user
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
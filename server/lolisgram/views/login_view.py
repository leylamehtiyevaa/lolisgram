from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from ..serializer.login_serializer import LoginSerializer

class UserLoginView(APIView):
    permission_classes = []
    serializer_class = LoginSerializer

    def post(self, request):
        """
        User login endpoint. Returns a user's access token.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']

            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
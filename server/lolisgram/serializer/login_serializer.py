from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model

class LoginSerializer(serializers.Serializer):
    """
    Serializer class for the User login.
    """
    email = serializers.CharField(max_length=100) # Kullanıcıdan e-posta almak için alan
    password = serializers.CharField(max_length=100, style={'input_type': 'password'}) # Kullanıcıdan şifre almak için alan


    def validate(self, data):
        """
        Validates the user with the entered email and password and returns errors.
        """
        email = data.get('email')
        password = data.get('password')
        User = get_user_model()

        if email and password:
            user = authenticate(request=self.context.get('request'), email=email, password=password)

            if user:
                data['user'] = user
            elif not user and User.objects.filter(email=email).exists():
                if not User.objects.get(email=email).is_active:
                    raise serializers.ValidationError('User account is inactive.')
                raise serializers.ValidationError('Incorrect password.')
            else:
                raise serializers.ValidationError('User does not exist.')

        return data
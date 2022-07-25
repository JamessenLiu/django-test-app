import jwt
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User


class JWTAuthentication(BaseAuthentication):

    def authenticate(self, request):
        auth_token = request.META.get('HTTP_AUTHTOKEN', "")
        try:
            payload = jwt.decode(auth_token, settings.SECRET_KEY, algorithms=['HS256'])
        except (jwt.DecodeError, jwt.InvalidTokenError):
            raise AuthenticationFailed('Invalid token')
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Token expired')

        username = payload.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise AuthenticationFailed("Unauthorized")

        return user, None

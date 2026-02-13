import hashlib
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone

from .models import APIKey


class APIKeyAuthentication(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get("X-API-KEY")

        if not api_key:
            return None  # Let other auth methods handle it

        key_hash = hashlib.sha256(api_key.encode()).hexdigest()

        try:
            key_obj = APIKey.objects.get(key_hash=key_hash)
        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")

        if key_obj.is_revoked:
            raise AuthenticationFailed("API Key has been revoked")

        if key_obj.expires_at and key_obj.expires_at < timezone.now():
            raise AuthenticationFailed("API Key has expired")

        return (key_obj.user, None)

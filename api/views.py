from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.utils import timezone
from datetime import timedelta

from .models import APIKey
from .authentication import APIKeyAuthentication


class CreateAPIKeyView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        raw_key, key_hash, prefix = APIKey.generate_key()

        expires_at = timezone.now() + timedelta(days=30)

        APIKey.objects.create(
            user=request.user,
            key_hash=key_hash,
            prefix=prefix,
            expires_at=expires_at
        )

        return Response({
            "success": True,
            "api_key": raw_key,
            "expires_at": expires_at.isoformat()
        }, status=status.HTTP_201_CREATED)


class SecureDataView(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "Secure data accessed successfully",
            "user": request.user.username
        })

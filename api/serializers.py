from rest_framework import serializers
from .models import APIKey


class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIKey
        fields = ["id", "prefix", "created_at", "expires_at", "is_revoked"]
        read_only_fields = ["id", "prefix", "created_at", "is_revoked"]

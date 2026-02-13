import uuid
import hashlib
import secrets
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class APIKey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="api_keys")

    prefix = models.CharField(max_length=8)
    key_hash = models.CharField(max_length=64)

    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    is_revoked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.prefix}"

    @staticmethod
    def generate_key():
        raw_key = "sk_live_" + secrets.token_hex(32)
        key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
        prefix = raw_key[:8]
        return raw_key, key_hash, prefix

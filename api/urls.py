from django.urls import path
from .views import CreateAPIKeyView, SecureDataView

urlpatterns = [
    path("keys/create/", CreateAPIKeyView.as_view()),
    path("secure-data/", SecureDataView.as_view()),
]

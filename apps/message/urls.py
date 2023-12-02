from django.urls import path
from .models import Message
from .views import ListMessageView
from .views import MessageListCreateAPIView

urlpatterns = [
    path("", ListMessageView.as_view(), name="list"),
    path("api/messages", MessageListCreateAPIView.as_view(), name="api"),
]

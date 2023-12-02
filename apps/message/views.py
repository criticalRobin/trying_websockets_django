from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.generics import ListCreateAPIView
from .models import Message
from .serializers import MessageSerializer
from django.views.generic import ListView
from rest_framework import generics


# Create your views here.
class ListMessageView(ListView):
    model = Message
    template_name = "message/list.html"


class MessageListCreateAPIView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "messages",
            {
                "type": "chat_message",
                "message": serializer.data[
                    "text"
                ],  # Asegúrate de que 'text' es el nombre correcto del campo en tu modelo.
            },
        )

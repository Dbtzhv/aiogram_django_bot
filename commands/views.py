from rest_framework.generics import ListAPIView
from .models import Command
from .serializers import CommandSerializer

class CommandListView(ListAPIView):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer

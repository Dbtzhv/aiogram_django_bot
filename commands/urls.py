from django.urls import path
from .views import CommandListView

urlpatterns = [
    path('commands/', CommandListView.as_view(), name='list_of_commands'),
]

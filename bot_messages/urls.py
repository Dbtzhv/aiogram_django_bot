from django.urls import path
from .views import TelegramMessageCreateView, TelegramMessageListView, chart_view

urlpatterns = [
    path('create_telegram_message/', TelegramMessageCreateView.as_view(), name='create_telegram_message'),
    path('user_messages/', TelegramMessageListView.as_view(), name='message-list'),
    path('chart/', chart_view, name='chart'),
]

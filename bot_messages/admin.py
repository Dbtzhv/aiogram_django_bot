from django.contrib import admin
from .models import TelegramMessage
from django.urls import reverse
from chartjs.views.lines import BaseLineChartView

@admin.register(TelegramMessage)
class TelegramMessageAdmin(admin.ModelAdmin):
    list_display = ('message_id', 'from_user_id', 'chat_id', 'text', 'created_at')
    list_filter = ('from_user_id', 'chat_id')
    search_fields = ('text', 'from_user_id', 'chat_id')  # Добавляем поля, по которым можно осуществлять поиск
    ordering = ('-created_at',)  # Сортировка по умолчанию: по дате создания в обратном порядке


#--------------------------------------------------------------
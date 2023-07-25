from django.db.models.functions import ExtractMonth
from django.db.models import Count
from .models import TelegramMessage

def get_message_count_by_month():
    message_count_by_month = TelegramMessage.objects.annotate(
        month=ExtractMonth('created_at')
    ).values('month').annotate(
        count=Count('id')
    ).order_by('month')

    month_counts = [0] * 12
    for entry in message_count_by_month:
        month = entry['month']
        count = entry['count']
        month_counts[month - 1] = count

    return tuple(month_counts)

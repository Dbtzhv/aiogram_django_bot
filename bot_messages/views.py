from rest_framework.generics import CreateAPIView, ListAPIView
from .models import TelegramMessage
from .serializers import TelegramMessageSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from drf_spectacular.openapi import OpenApiParameter
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from .services import get_message_count_by_month


class TelegramMessageCreateView(CreateAPIView):
    queryset = TelegramMessage.objects.all()
    serializer_class = TelegramMessageSerializer


@extend_schema_view(
    get=extend_schema(
        parameters=[
            OpenApiParameter(name='from_user_id', description='User Id', type=int),
        ]
    )
)
class TelegramMessageListView(ListAPIView):
    serializer_class = TelegramMessageSerializer

    def get_queryset(self):
        from_user_id = self.request.query_params.get('from_user_id')
        if from_user_id:
            queryset = TelegramMessage.objects.filter(from_user_id=from_user_id)
        else:
            queryset = TelegramMessage.objects.all()
        return queryset



from django.shortcuts import render

def chart_view(request):
    if not request.user.is_superuser:
        return render(request, 'access_denied.html')
        
    data = get_message_count_by_month()
    return render(request, 'message_count_chart.html', {'data': data})

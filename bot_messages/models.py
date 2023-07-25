from django.db import models

class TelegramMessage(models.Model):
    message_id = models.IntegerField()
    from_user_id = models.IntegerField()
    chat_id = models.IntegerField()
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.from_user_id}, Message: {self.text[:30]}..."

    class Meta:
        app_label = 'bot_messages'



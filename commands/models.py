from django.db import models

class Command(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Command: {self.title}"

    class Meta:
        app_label = 'commands'



from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notifications")
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    url = models.CharField(null=True, blank=True, max_length=255)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return f"notifications for {self.user.username}"
    
    
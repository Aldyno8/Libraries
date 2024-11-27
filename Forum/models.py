from django.db import models
from django.contrib.auth.models import User

class ForumSubject(models.Model):
    subject = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.subject
    
    
class ForumMessage(models.Model):
    subject = models.ForeignKey(ForumSubject, on_delete=models.CASCADE, related_name="message")
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author} : {self.message}"
    
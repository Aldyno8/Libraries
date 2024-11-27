from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ForumMessage 
from Notifications.models import Notification

@receiver(post_save, sender=ForumMessage)
def createNotification(sender, instance, created, **kwargs):
    if created:
        subject_author = instance.subject.creator
        if subject_author != instance.author:
            try:
                Notification.objects.create(
                    user=subject_author,
                    message=f"{instance.author} vous a repondu a concernant {instance.subject}",
                    url=f"forum/details/{instance.subject.id}/"
                )
            except Exception as error:
                return str(error)
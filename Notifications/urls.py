from rest_framework.urls import path
from .views import NotificationListView, ReadNotifications

urlpatterns = [
    path("list/", NotificationListView.as_view(), name="notification_list"),
    path("update/<int:pk>/", ReadNotifications.as_view(), name="read")
]

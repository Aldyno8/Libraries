from rest_framework.urls import path
from .views import *

urlpatterns = [
    path("create/",CreateForum.as_view(), name="create_forum"),
    path("message/",CreateMessage.as_view(), name="create_message"),
    path("list/",ForumListView.as_view(), name="list_forum"),
    path("details/<int:pk>/", ForumDetails.as_view(), name="details"),
]

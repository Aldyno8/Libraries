from django.contrib import admin
from .models import *

admin.site.register(ForumMessage),
admin.site.register(ForumSubject)


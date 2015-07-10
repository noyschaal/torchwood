from django.contrib import admin

from .models import Topic
from .models import TopicEntry
from .models import PrivateEntry
 
admin.site.register(Topic)
admin.site.register(TopicEntry)
admin.site.register(PrivateEntry)
# Register your models here.

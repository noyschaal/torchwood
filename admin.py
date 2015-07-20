from django.contrib import admin
from .models import UserProfile, MentorGroup, Topic, TopicEntry, PrivateEntry, UserToGroup

admin.site.register(MentorGroup)
admin.site.register(UserProfile)
admin.site.register(Topic)
admin.site.register(TopicEntry)
admin.site.register(PrivateEntry)
admin.site.register(UserToGroup)


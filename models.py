from django.db import models
from django.contrib.auth.models import Group, User

#for images
class UserProfile(models.Model):
    user   = models.OneToOneField('auth.User', default='999')
    avatar = models.ImageField()

#Group 
class MentorGroup(models.Model):
	name = models.CharField(max_length=50)
	description = models.CharField(max_length=200)
	mentorID = models.ManyToManyField('auth.User', default='999')
	def __unicode__(self):
		return self.name
		
#UserToGroup
class UserToGroup(models.Model):
	user = models.ForeignKey('auth.User', default='999')
	group = models.ForeignKey('MentorGroup', default='999')

#Topic		
class Topic(models.Model):
	mentor = models.ForeignKey('auth.User', default='999')
	group = models.ForeignKey('MentorGroup', default='999')
	title = models.CharField(max_length=100)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.title

#Entry for a topic
class TopicEntry(models.Model):
	topic = models.ForeignKey('Topic', default='999')
	user = models.ForeignKey('auth.User', default='999')
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)
	def __unicode__(self):
		return self.topic.title

#Private entries		
class PrivateEntry(models.Model):
	user = models.OneToOneField('auth.User', default='999')
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)



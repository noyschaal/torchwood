from django.db import models

class Topic(models.Model):
        title = models.CharField(max_length=200)
        content = models.CharField(max_length=500)
        date = models.DateTimeField()
	def __str__(self):
		return self.content

class TopicEntry(models.Model):
	content = models.CharField(max_length=500)
	topic = models.ForeignKey(Topic)
	date = models.DateTimeField()
	def __str__(self):
		return self.content
	
class PrivateEntry(models.Model):
        content = models.CharField(max_length=500)
        date = models.DateTimeField()


# Create your models here.


from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    body = models.TextField()
    tagnames = models.CharField(max_length=125)
    author = models.CharField(max_length=125)
    added_at = models.DateTimeField(default=datetime.datetime.now)
    score = models.IntegerField(default=0)
    answer_count = models.IntegerField(null=True)
    
    def __str__(self):
        return self.body
    def split_tags(self):
        """Splits the tagnames when they are separated by comma"""
        return self.tagnames.split(',')
        
		
class Answer(models.Model):
    question = models.ForeignKey(Question)
    body = models.TextField()
    author = models.CharField(max_length=125)
    added_at = models.DateTimeField(default=datetime.datetime.now)
    score = models.IntegerField(default=0)
	
    def __str__(self):
        return self.body
		

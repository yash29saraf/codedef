from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

YEAR = (  
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
)
TOPICS = (  
    ('Searching', 'Searching'),
    ('Sorting', 'Sorting'),
    ('DP', 'DP'),
)
class Topics(models.Model):
    name=models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
class Knowledge(models.Model):
    name=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    year=models.CharField(max_length=100,choices=YEAR)
    #year=models.IntegerField()
    phone=models.CharField(max_length=12)
    email=models.EmailField()
    topics=models.ManyToManyField(Topics)
    #topics=models.TextField()
    language=models.BooleanField()
    workshop=models.BooleanField()
    
    def __unicode__(self):
        return self.name


'''class Knowledge(models.Model):
	name=models.CharField(max_length=200)
	branch=models.CharField(max_length=200)
    year=models.IntegerField()
    #year=models.IntegerField()
    #phone=models.IntegerField()
    #email=models.EmailField()
    #topics=models.TextField()
	
    def __unicode__(self):
		return self.title
    '''
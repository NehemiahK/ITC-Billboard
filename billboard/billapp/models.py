# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.



class Post(models.Model):
    #published_date = models.DateTimeField()
    #the fields that are saved

    title = models.CharField(max_length=500)
    text = models.TextField()
    author = models.CharField(max_length=500)

    def __str__(self):
        return self.title+" by "+self.author

# class Create_User(models.Model):
#
#     user = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#     password_confimation = models.CharField(max_length=30)

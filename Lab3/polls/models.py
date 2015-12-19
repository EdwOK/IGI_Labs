from __future__ import unicode_literals
import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone


class Question(models.Model):
    author = models.ForeignKey(User)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text

    def __unicode__(self):
        return self.question_text

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def __unicode__(self):
        return self.choice_text


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    author = models.ForeignKey(User)
    create_date = models.DateTimeField('create date', default=timezone.now)

    def __str__(self):
        return self.content

    def __unicode__(self):
        return self.content

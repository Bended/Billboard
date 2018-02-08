# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import date

# Create your models here.
@python_2_unicode_compatible
class Messages(models.Model):
    msg_date = models.DateField(("Date"), auto_now_add=True,)
    msg_title = models.CharField(max_length=200)
    msg = models.CharField(max_length=2000)
    msg_author = models.CharField(max_length=50)
    def __str__(self):
        return "msg_date = %s, msg_title = %s, msg_author= %s" % (self.msg_date, self.msg_title, self.msg_author)
#!/usr/bin/env python
# (c) 2017 CJ Associates
#
from django.db import models

class President(models.Model):
    termnum = models.IntegerField()
    firstname = models.CharField(max_length=32)
    lastname = models.CharField(max_length=32)
    birthplace = models.CharField(max_length=32)
    birthstate = models.CharField(max_length=32)
    birthdate = models.DateField()
    deathdate = models.DateField()
    termstart = models.DateField()
    termend = models.DateField()
    party = models.CharField(max_length=32)

    def __str__(self):
        return '{} {}'.format(self.firstname, self.lastname)


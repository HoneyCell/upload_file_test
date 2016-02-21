from __future__ import unicode_literals

from django.db import models

# Create your models here.




class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __unicode__(self):
        return "New student: %s %s" %(self.first_name, self.last_name)



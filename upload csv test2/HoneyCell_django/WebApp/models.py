from __future__ import unicode_literals

from django.db import models

# Create your models here.

class MyCsvModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=100)

    class Meta:
        delimiter = ";"


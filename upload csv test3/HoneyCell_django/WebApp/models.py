from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Job(models.Model):
    job_id = models.CharField(max_length=100)
    job_file = models.FileField(upload_to="file_folder/")
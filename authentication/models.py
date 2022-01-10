from django.db import models
from django.contrib import auth
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User






# Create your models here.
class ProjectMaster(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
         on_delete = models.CASCADE)
    project_name=models.CharField(max_length=50)

    def __str__(self):
        return self.project_name


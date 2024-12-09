from django.db import models


# Create your models here.
class Task(models.Model):
    Title = models.CharField(max_length=300)

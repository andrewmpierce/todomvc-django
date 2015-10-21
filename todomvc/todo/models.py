from django.db import models

# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    #id = models.PositiveSmallIntegerField(primary_key=True)
    order = models.PositiveSmallIntegerField(null = True)

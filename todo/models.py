from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    deadline = models.DateTimeField()
    asignee = models.ForeignKey(User, on_delete = models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)

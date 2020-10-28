from django.db import models


class Todo(models.model):
    name = models.CharField(max_length=120)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

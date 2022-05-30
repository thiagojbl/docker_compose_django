from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    content = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

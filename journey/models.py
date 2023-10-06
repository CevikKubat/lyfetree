from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # Add other fields as needed

    def __str__(self):
        return self.name

class Milestone(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)  # Many-to-many relationship with tags
    date_created = models.DateTimeField(default=timezone.now)
    date_last_changed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

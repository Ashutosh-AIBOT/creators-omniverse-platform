from django.db import models
from django.contrib.auth.models import User
import uuid

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class CommunityGroup(models.Model):
    PRIVACY_CHOICES = [
        ('public', 'Public'),
        ('private', 'Private'),
    ]
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='groups')
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=10, unique=True, blank=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_groups')
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='public')
    description = models.TextField(blank=True)
    
    members = models.ManyToManyField(User, related_name='joined_groups', blank=True)
    ignored_by = models.ManyToManyField(User, related_name='ignored_groups', blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.unique_id:
            self.unique_id = str(uuid.uuid4())[:8].upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.unique_id})"

class Message(models.Model):
    group = models.ForeignKey(CommunityGroup, on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']

    def __str__(self):
        return f"{self.user.username}: {self.content[:20]}"

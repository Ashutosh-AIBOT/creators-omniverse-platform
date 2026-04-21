from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    about = models.TextField(blank=True, null=True)  # About section
    is_public = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    
    resume_url = models.URLField(blank=True, null=True)
    resume_is_public = models.BooleanField(default=False)

    # Store multiple skills and current roles as newline-separated text
    skills = models.TextField(blank=True, null=True)
    currently = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(default=timezone.now)  # Changed from auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"

    # Helper methods to get lists of skills and currently working roles
    def get_skills_list(self):
        if self.skills:
            return [skill.strip() for skill in self.skills.split('\n') if skill.strip()]
        return []

    def get_currently_list(self):
        if self.currently:
            return [role.strip() for role in self.currently.split('\n') if role.strip()]
        return []


class LinkItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='link_items')
    section = models.CharField(max_length=50)
    title = models.CharField(max_length=255)        # Name of the link item
    description = models.TextField(blank=True)      # Description
    url = models.URLField()
    button_text = models.CharField(max_length=100, default="Visit")  # Button text shown on frontend
    is_public = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(default=timezone.now)  # Changed from auto_now_add=True
    updated_at = models.DateTimeField(auto_now=True)      # Track updates
    
    def __str__(self):
        return f"{self.title} ({self.section})"

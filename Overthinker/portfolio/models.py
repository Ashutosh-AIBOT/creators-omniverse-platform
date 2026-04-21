from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# ---------- Image size validation ----------
def validate_image_size(image):
    if image.size > 80 * 1024:
        raise ValidationError("Image must be less than 80KB")


def project_image_path(instance, filename):
    return f'projects/user_{instance.portfolio.user.id}/{filename}'


THEME_CHOICES = [
    ('theme1', 'Clean Light'),
    ('theme2', 'Dark Professional'),
    ('theme3', 'Modern Gradient'),
]


class Portfolio(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=150)
    headline = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)
    bio = models.CharField(max_length=250, blank=True)
    about = models.TextField()

    theme = models.CharField(
        max_length=20,
        choices=THEME_CHOICES,
        default='theme1'
    )

    is_public = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} Portfolio"


class Project(models.Model):
    portfolio = models.ForeignKey(
        Portfolio,
        on_delete=models.CASCADE,
        related_name='projects'
    )

    name = models.CharField(max_length=200)
    link = models.URLField()
    image = models.ImageField(
        upload_to=project_image_path,
        blank=True,
        null=True,
        validators=[validate_image_size]
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

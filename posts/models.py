import uuid

from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    social_email = models.CharField(max_length=200, blank=True)
    social_github = models.CharField(max_length=200, blank=True)
    social_facebook = models.CharField(max_length=200, blank=True)
    social_linkedin = models.CharField(max_length=200, blank=True)
    social_instagram = models.CharField(max_length=200, blank=True)
    social_website = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True, null=True)
    post_img = models.ImageField(upload_to='post/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.name}"

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

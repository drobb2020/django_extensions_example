from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', default="profile/avatar.jpg")
    social_email = models.CharField(max_length=200, default="", blank=True)
    social_github = models.CharField(max_length=200, default="", blank=True)
    social_facebook = models.CharField(max_length=200, default="", blank=True)
    social_linkedin = models.CharField(max_length=200, default="", blank=True)
    social_instagram = models.CharField(max_length=200, default="", blank=True)
    social_portfolio = models.CharField(max_length=200, default="", blank=True)
    social_digital_resume = models.CharField(max_length=200, default="", blank=True)

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=get_user_model())
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()

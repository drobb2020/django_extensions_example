from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            "email",
            "username",
        )


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            "name",
            "bio",
            "profile_pic",
            "social_email",
            "social_github",
            "social_facebook",
            "social_linkedin",
            "social_instagram",
            "social_portfolio",
            "social_digital_resume",
        )

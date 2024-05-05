from django import forms

from .models import Post, Review


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "snippet", "body", "post_img")


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "author", "snippet", "body", "post_img")


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("post", "review", "author")

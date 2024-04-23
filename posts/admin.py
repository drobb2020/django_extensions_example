# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Author, Post


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'social_email',
        'social_github',
        'social_facebook',
        'social_linkedin',
        'social_instagram',
        'social_website',
    )
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'author',
        'snippet',
        'updated',
    )
    list_filter = ('date', 'author', 'updated')

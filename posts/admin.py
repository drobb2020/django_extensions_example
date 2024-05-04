# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Post, Review


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'date',
        'author',
        'snippet',
        'body',
        'post_img',
        'updated',
    )
    list_filter = ('date', 'author', 'updated')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'review', 'rating', 'author')
    list_filter = ('post', 'author')

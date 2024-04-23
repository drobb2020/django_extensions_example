# from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostCreateForm, PostUpdateForm
from .models import Post


class PostsListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/post_create.html"
    form_class = PostCreateForm


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    form_class = PostUpdateForm


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")

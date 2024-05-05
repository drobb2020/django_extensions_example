# from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import PostCreateForm, PostUpdateForm, ReviewCreateForm
from .models import Post, Review


class PostsListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "posts/post_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
    queryset = Post.objects.all().prefetch_related('reviews__post',)


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


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = "posts/review_create.html"
    success_url = reverse_lazy("post_list")


class SearchResultsListView(ListView):
    model = Post
    context_object_name = "post_list"
    template_name = "posts/search_results.html"

    def queryset(self):
        query = self.request.GET.get("q")
        return Post.objects.filter(
            Q(title__icontains=query) | Q(body__icontains=query)
        )

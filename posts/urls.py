from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostsListView.as_view(), name="post_list"),
    path("<uuid:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("post_create/", views.PostCreateView.as_view(), name="post_create"),
    path("post_update/<uuid:pk>/", views.PostUpdateView.as_view(), name="post_update"),
    path("post_delete/<uuid:pk>/", views.PostDeleteView.as_view(), name="post_delete"),
    path("review_create/", views.ReviewCreateView.as_view(), name="review_create"),
    path("search/", views.SearchResultsListView.as_view(), name="search_results"),
]

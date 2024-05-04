from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CustomUserCreationForm, ProfileUpdateForm
from .models import Profile


class SignupPageView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ProfilePageView(ListView):
    model = Profile
    context_object_name = "profile"
    template_name = "account/profile.html"


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    success_url = reverse_lazy("profile")
    template_name = "account/profile_update.html"

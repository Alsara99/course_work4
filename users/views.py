from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import (
    CustomUserCreationForm,
    CustomAuthenticationForm,
    UserProfileForm
)

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mailing:index')
    template_name = 'users/register.html'

class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('mailing:index')

class CustomLogoutView(LogoutView):
    next_page = '/'

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/profile_detail.html'
    context_object_name = 'user_obj'

    def get_object(self):
        return self.request.user


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserProfileForm
    template_name = 'users/profile_form.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        return self.request.user
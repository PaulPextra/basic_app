from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from core.forms import UserProfileCreationForm

User = get_user_model()

class SignUpView(CreateView):
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class HomeView(TemplateView, LoginRequiredMixin):
  template_name = 'home.html'
  
class ProfileView(TemplateView, LoginRequiredMixin):
  template_name = 'profile.html'
  
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
  template_name = 'profile_edit.html'
    
    



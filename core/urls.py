from django.urls import path
from core.views import HomeView, ProfileView, ProfileUpdateView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomeView.as_view(), name='home'),
    path('user/profile/', ProfileView.as_view(), name='profile'),
    path('user/profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
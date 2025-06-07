# user_app/urls.py
from django.urls import path
from .views import SignupView, ProfileView
from django.contrib.auth import views as auth_views

app_name = 'user_app'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
]
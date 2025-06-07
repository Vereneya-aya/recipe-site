from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from recipe_app.models import Recipe
from .forms import CustomUserCreationForm

from django.views import View
from django.contrib.auth import login

class SignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'user_app/signup.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('recipes_list')
        return render(request, 'user_app/signup.html', {'form': form})

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        recipes = Recipe.objects.filter(author=request.user)
        # если будут лайки, можно добавить liked_recipes
        return render(request, 'user_app/profile.html', {
            'recipes': recipes
        })

class MyLogoutPage(View):
    def get(self, request):
        logout(request)
        return redirect('user_app:login')
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Recipe
from .forms import RecipeForm


class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipe_app/recipes_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(archived=False)


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_app/recipe_detail.html'
    context_object_name = 'recipe'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_app/create_recipe.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_app:recipe_detail', kwargs={'pk': self.object.pk})


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_app/update_recipe.html'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse_lazy('recipe_app:recipe_detail', kwargs={'pk': self.object.pk})


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_app/confirm_delete.html'
    success_url = reverse_lazy('recipe_app:recipes_list')

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)


class RecipeArchiveView(LoginRequiredMixin, View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
        return render(request, 'recipe_app/confirm_archive.html', {'recipe': recipe})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
        recipe.archived = True
        recipe.save()
        return redirect('recipe_app:recipes_list')


def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'recipe_app/groups.html', {'groups': groups})
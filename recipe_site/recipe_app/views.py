import logging
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import RecipeForm
from .models import Recipe, Category

logger = logging.getLogger(__name__)


from django.views.generic import ListView
from .models import Recipe, Category
import random

class RecipesListView(ListView):
    model = Recipe
    template_name = 'recipe_app/recipes_list.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        return Recipe.objects.filter(archived=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_recipes = list(Recipe.objects.filter(archived=False))
        random.shuffle(all_recipes)
        context['random_recipes'] = all_recipes[:5]

        # все категории — для фильтра
        context['categories'] = Category.objects.all()
        return context

class RecipesByCategoryView(ListView):
    model = Recipe
    template_name = 'recipe_app/recipes_by_category.html'
    context_object_name = 'recipes'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Recipe.objects.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_app/recipe_detail.html'
    context_object_name = 'recipe'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        logger.info(f"[{self.request.user}] просматривает рецепт: {obj.name} (ID={obj.id})")
        return obj


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_app/create_recipe.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info(f"[{self.request.user}] создаёт рецепт: {form.instance.name}")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_app:recipe_detail', kwargs={'pk': self.object.pk})


class RecipeUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_app/update_recipe.html'

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

    def form_valid(self, form):
        logger.info(f"[{self.request.user}] обновляет рецепт: {form.instance.name} (ID={form.instance.id})")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('recipe_app:recipe_detail', kwargs={'pk': self.object.pk})


class RecipeDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipe
    template_name = 'recipe_app/confirm_delete.html'
    success_url = reverse_lazy('recipe_app:recipes_list')

    def get_queryset(self):
        return Recipe.objects.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        logger.info(f"[{request.user}] удаляет рецепт: {obj.name} (ID={obj.id})")
        return super().delete(request, *args, **kwargs)


class RecipeArchiveView(LoginRequiredMixin, View):
    def get(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
        logger.info(f"[{request.user}] открыл страницу архивации рецепта: {recipe.name}")
        return render(request, 'recipe_app/confirm_archive.html', {'recipe': recipe})

    def post(self, request, pk):
        recipe = get_object_or_404(Recipe, pk=pk, author=request.user)
        recipe.archived = True
        recipe.save()
        logger.info(f"[{request.user}] архивировал рецепт: {recipe.name} (ID={recipe.id})")
        return redirect('recipe_app:recipes_list')


def group_list(request):
    logger.info(f"[{request.user}] просматривает список групп")
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'recipe_app/groups.html', {'groups': groups})
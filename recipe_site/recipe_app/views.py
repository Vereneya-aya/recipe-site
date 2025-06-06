from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from .models import Recipe
from .utils import with_timer  # Декоратор для измерения времени
from .forms import RecipeForm

# Главная страница с тестовыми рецептами (строками)
@with_timer
def recipe_index(request):
    recipes = ['Борщ', 'Плов', 'Оливье', 'Шакшука']
    context = {
        'recipes': recipes
    }
    return request, 'recipe_app/recipe_index.html', context

# Страница с рецептами из модели
@with_timer
def recipes_list(request):
    recipes = Recipe.objects.filter(archived=False)
    context = {
        'recipes': recipes
    }
    return request, 'recipe_app/recipes_list.html', context

# Страница групп пользователей
def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'recipe_app/groups.html', {'groups': groups})


#liked_by = models.ManyToManyField(User, related_name='liked_recipes', blank=True)
@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)  # или куда тебе нужно
    else:
        form = RecipeForm()
    return render(request, 'recipe_app/create_recipe.html', {'form': form})
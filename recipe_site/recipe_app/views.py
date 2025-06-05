from django.shortcuts import render
from timeit import default_timer as timer

def recipe_index(request):
    start = timer()

    recipes = ['Борщ', 'Плов', 'Оливье', 'Шакшука']

    end = timer()
    elapsed_time = end - start

    context = {
        'recipes': recipes,
        'time_running': round(elapsed_time, 5)
    }
    return render(request, 'recipe_app/recipe_index.html', context)

from django.shortcuts import render
from django.contrib.auth.models import Group

def group_list(request):
    groups = Group.objects.prefetch_related('permissions').all()
    return render(request, 'recipe_app/groups.html', {'groups': groups})
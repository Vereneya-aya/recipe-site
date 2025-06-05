from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.group_list, name='group_list'),
    path('', views.recipe_index, name='recipe_index'),
    path('recipes/', views.recipes_list, name='recipes_list'),  # <--- добавили этот

]
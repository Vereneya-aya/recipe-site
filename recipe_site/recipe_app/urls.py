from django.urls import path
from .views import RecipesListView, RecipeCreateView, RecipeDetailView, group_list, RecipeUpdateView, RecipeDeleteView, \
    RecipeArchiveView

app_name = 'recipe_app'

urlpatterns = [
    path('', RecipesListView.as_view(), name='recipes_list'),                        # /
    path('create/', RecipeCreateView.as_view(), name='create_recipe'),              # /create/
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),    # /recipes/1/
    path('groups/', group_list, name='group_list'),
    path('recipes/<int:pk>/edit/', RecipeUpdateView.as_view(), name='update_recipe'),# /groups/
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='confirm_delete'),
    path('recipes/<int:pk>/archive/', RecipeArchiveView.as_view(), name='confirm_archive'),

]
# recipe_app/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import RecipeViewSet

router = DefaultRouter()
router.register(r'recipes', RecipeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
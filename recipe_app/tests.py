from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Recipe

User = get_user_model()

class RecipeModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.recipe = Recipe.objects.create(
            name='Test Recipe',
            description='Delicious test recipe',
            ingredients='Eggs, Milk, Flour',
            instructions='Mix and bake.',
            cooking_time=30,
            author=self.user
        )

    def test_recipe_creation(self):
        self.assertEqual(self.recipe.name, 'Test Recipe')
        self.assertEqual(self.recipe.author.username, 'testuser')
        self.assertFalse(self.recipe.archived)
        self.assertIn('Delicious', self.recipe.description)
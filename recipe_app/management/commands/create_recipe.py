from django.core.management.base import BaseCommand
from recipe_app.models import Recipe

class Command(BaseCommand):
    help = 'Создает несколько рецептов, если они ещё не существуют'

    def handle(self, *args, **kwargs):
        recipes_data = [
            {
                'name': 'Шоколадный торт',
                'description': 'Очень вкусный торт с шоколадом и орехами',
                'cooking_time': 60
            },
            {
                'name': 'Овощной суп',
                'description': 'Лёгкий суп с сезонными овощами',
                'cooking_time': 30
            },
            {
                'name': 'Паста с томатным соусом',
                'description': 'Итальянская паста с насыщенным соусом',
                'cooking_time': 25
            }
        ]

        for recipe_data in recipes_data:
            recipe, created = Recipe.objects.get_or_create(
                name=recipe_data['name'],
                defaults={
                    'description': recipe_data['description'],
                    'cooking_time': recipe_data['cooking_time']
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Создан: {recipe.name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Уже существует: {recipe.name}'))
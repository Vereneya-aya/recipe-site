from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField(blank=True)  # Новый блок
    instructions = models.TextField(blank=True)  # Новый блок
    cooking_time = models.IntegerField()  # в минутах
    archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    likes = models.ManyToManyField(User, related_name='liked_recipes', blank=True)

    def __str__(self):
        return f"{self.name} ({self.cooking_time} мин)"

    def short_description(self):
        return self.description[:50] + '...' if len(self.description) > 50 else self.description

    short_description.short_description = "Краткое описание"

    class Meta:
        ordering = ['-created_at']  # по убыванию даты создания
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='likes_by')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'recipe')  # запретить повторный лайк

    def __str__(self):
        return f'{self.user.username} ❤️ {self.recipe.name}'
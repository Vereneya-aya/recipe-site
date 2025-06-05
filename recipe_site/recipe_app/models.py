from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    cooking_time = models.IntegerField()  # в минутах
    archived = models.BooleanField(default=False)  # "удалён" или нет
    created_at = models.DateTimeField(auto_now_add=True)  # время создания

    def __str__(self):
        return self.name

eated_at = models.DateTimeField(auto_now_add=True)
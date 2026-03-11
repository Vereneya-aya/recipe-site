from django.contrib import admin
from .models import Recipe, Like
from .admin_mixins import ExportAsCSVMixin


@admin.action(description='Архивировать выбранные рецепты')
def archive_selected(modeladmin, request, queryset):
    updated = queryset.update(archived=True)
    modeladmin.message_user(request, f"{updated} рецептов архивировано.")


@admin.action(description='Разархивировать выбранные рецепты')
def unarchive_selected(modeladmin, request, queryset):
    updated = queryset.update(archived=False)
    modeladmin.message_user(request, f"{updated} рецептов разархивировано.")


@admin.register(Recipe)
class RecipeAdmin(ExportAsCSVMixin, admin.ModelAdmin):  # ← добавлен миксин
    list_display = ('name', 'author', 'cooking_time', 'archived', 'created_at')
    list_filter = ('archived', 'created_at')
    search_fields = ('name', 'description', 'author__username')
    ordering = ('-created_at',)
    actions = [archive_selected, unarchive_selected, 'export_as_csv']  # ← 3 действия

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'cooking_time')
        }),
        ('Дополнительные параметры', {
            'classes': ('collapse',),
            'fields': ('archived', 'created_at', 'author'),
        }),
    )

    readonly_fields = ('created_at',)

from .models import Category  # ← добавь импорт

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe', 'created_at')
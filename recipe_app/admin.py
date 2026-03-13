from django.contrib import admin
from .models import Recipe, Category, Like
from .admin_mixins import ExportAsCSVMixin


# ---------- Admin Actions ----------

@admin.action(description="Archive selected recipes")
def archive_selected(modeladmin, request, queryset):
    updated = queryset.update(archived=True)
    modeladmin.message_user(request, f"{updated} recipes archived.")


@admin.action(description="Unarchive selected recipes")
def unarchive_selected(modeladmin, request, queryset):
    updated = queryset.update(archived=False)
    modeladmin.message_user(request, f"{updated} recipes restored.")


# ---------- Recipe Admin ----------

@admin.register(Recipe)
class RecipeAdmin(ExportAsCSVMixin, admin.ModelAdmin):
    list_display = (
        "name",
        "author",
        "cooking_time",
        "archived",
        "created_at",
    )

    list_filter = (
        "archived",
        "created_at",
        "author",
        "categories",
    )

    search_fields = (
        "name",
        "description",
        "ingredients",
        "author__username",
    )

    ordering = ("-created_at",)

    readonly_fields = (
        "created_at",
    )

    filter_horizontal = (
        "categories",
        "likes",
    )

    actions = (
        archive_selected,
        unarchive_selected,
        "export_as_csv",
    )

    fieldsets = (
        ("Recipe", {
            "fields": (
                "name",
                "author",
                "categories",
            )
        }),

        ("Content", {
            "fields": (
                "description",
                "ingredients",
                "instructions",
            )
        }),

        ("Cooking", {
            "fields": (
                "cooking_time",
                "image",
            )
        }),

        ("Status", {
            "classes": ("collapse",),
            "fields": (
                "archived",
                "created_at",
                "likes",
            ),
        }),
    )


# ---------- Category Admin ----------

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# ---------- Like Admin ----------

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "recipe",
        "created_at",
    )

    search_fields = (
        "user__username",
        "recipe__name",
    )

    list_filter = (
        "created_at",
    )
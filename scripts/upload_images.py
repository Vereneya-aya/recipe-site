import os
from recipe_app.models import Recipe
from django.core.files import File

MEDIA_ROOT = "media"

for r in Recipe.objects.all():
    if r.image:
        file_path = os.path.join(MEDIA_ROOT, r.image.name)

        if os.path.exists(file_path):
            print("Uploading:", file_path)

            with open(file_path, "rb") as f:
                r.image.save(os.path.basename(r.image.name), File(f), save=True)
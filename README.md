Project “Recipe Website” (Django)

This is a Django web application that allows users to add, view, and manage recipes.

🚀 Features
	•	User registration, login, and logout
	•	Viewing a list of recipes and detailed recipe pages
	•	Adding, editing, and deleting recipes
	•	Archiving recipes
	•	Liking recipes
	•	User profile with their own recipes

🧱 Tech Stack
	•	Python 3.10+
	•	Django 5.2
	•	SQLite
	•	HTML / CSS (Bootstrap)

📂 Project Structure

RecipesPythonDjango/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── recipe_site/
│   ├── mysite/
│   │   ├── settings.py
│   │   └── urls.py
│   └── recipe_app/
│       ├── templates/recipe_app/
│       │   ├── base.html
│       │   ├── recipes_list.html
│       │   ├── recipe_detail.html
│       │   ├── create_recipe.html
│       │   ├── update_recipe.html
│       │   ├── confirm_delete.html
│       │   ├── confirm_archive.html
│       │   └── groups.html
│       ├── models.py
│       ├── views.py
│       ├── forms.py
│       └── urls.py
└── user_app/
    ├── templates/user_app/
    │   ├── login.html
    │   ├── logout.html
    │   ├── signup.html
    │   └── profile.html 
    ├── views.py
    ├── forms.py
    └── urls.py

⚙️ Installation & Running the Project

	1.	Clone the repository
git clone https://github.com/Vereneya-aya/recipe-site.git
cd RecipesPythonDjango

	2.	Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate


	3.	Install dependencies
pip install -r requirements.txt


	4.	Apply migrations and create a superuser
python manage.py migrate
python manage.py createsuperuser


	5.	(Optional) Load fixtures with sample recipes
python manage.py loaddata recipes.json


	6.	Run the server
python manage.py runserver

📥 Fixtures
The fixtures can be found in the recipes.json file inside the fixtures/ directory.

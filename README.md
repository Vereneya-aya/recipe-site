# Проект "Сайт рецептов" (Django)

Это веб-приложение на Django, позволяющее пользователям добавлять, просматривать и управлять рецептами.

## 🚀 Возможности
- Регистрация, вход, выход
- Просмотр списка рецептов и детальной информации
- Добавление, редактирование, удаление рецептов
- Архивация рецептов
- Лайки на рецепты
- Профиль пользователя с его рецептами

## 🧱 Стек технологий
- Python 3.10+
- Django 5.2
- SQLite
- HTML / CSS (Bootstrap)

## 📂 Структура проекта

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


## ⚙️ Установка и запуск проекта

1. **Клонировать репозиторий**

git clone https://github.com/Vereneya-aya/recipe-site.git
cd RecipesPythonDjango

2.	Создать и активировать виртуальное окружение

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

3.	Установить зависимости

pip install -r requirements.txt

4. Применить миграции и создать суперпользователя

python manage.py migrate
python manage.py createsuperuser

5.	(опционально) Загрузить фикстуры с рецептами

python manage.py loaddata recipes.json

6.	Запустить сервер

python manage.py runserver

📥 Фикстуры

Фикстуры можно найти в файле recipes.json в директории fixtures/.

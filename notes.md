Steps:
1) Create dir, create venv
2) Create git repo
3) Create gitignore file
4) Install django for venv pip:
```pip install django```
5) Initialize project
```django-admin startproject btre .```
6) Create 'pages' app
```python manage.py startapp pages```
7) Create 'urls.py' file in 'pages' app

Django tips:
- django-admin help - список всіх команд від django
- django-admin startproject btre . - ініціалізація проекту
- python manage.py runserver - запустити сервер
- https://gitignore.io - генерує за тегами
- settings.py - файл конфігурації проекту. Містить:
    + шлях до директорії проєкту
    + SECRET_KEY - ключ, треба сховати при деплої
    + DEBUG - при деплої поставити False, відображати помилки, при цьому ввести в ALLOWED_HOSTS доменне ім'я або ip адресу
    + INSTALLED_APPS - список всіх застосунків, що є в проєкті
    + ROOT_URLCONF - базовий файл з url, з якого починається пошук при запиті
    + та інше(налаштування БД, список шаблонів, валідатори паролів)
    + STATIC - шлях до директорії з статичними файлами

- urls.py містить список всіх urls, які оброблює. Може містити посилання на urls.py іншого застосунку, в якому окремо urls.py визначений
Після створення urls.py необхідно приєднати його до загального ROOT_URLCONF (додати в urlspatterns list):
```
path('', include('pages.urls'))
```
urls.py містить список урлів, які має оброблювати та посилання на класи та функції в views.py
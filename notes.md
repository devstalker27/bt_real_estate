## Steps
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
8) Create templates dir in base dir with subdirs with our apps
9) Create html files, which need to render
10) Add in settings path to templates dir
11) Add to urls new routes, add views with render
12) Create base.html з базовим дизайном html сторінки, від якого інші будуть наслідуватися
13) Add static files [some in btre dir with name static] and add to settings.py static settings. After all type: python manage.py collectstatic
14) Add base template html code with partials files




### Django tips
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

- Щоб рендерити сторінку html, треба в views використати метод render:
```
return render(request=request, 'app_name/page_name.html')
```

- На самому початку треба розробити базові шаблони, від яких потім можна наслідувати html сторінки інших застосунків.

В базовому шаблоні треба визначити, де буде вставка, яку будуть реалізовувати ті, хто наслідує базовий шаблон
```
<body>
    {%block content%} Тут буде те, що реалізовують шаблони {% endblock %}
</body>
```

- В шаблоні, що наслідується від базового, необхідно вказати, що це буде реалізація шаблону
```
{% extends 'base.html' %}
{% block content %}

<h1>Тут буде те, що доповнює саме цей шаблон</h1>

{% endblock content %}

```

- Jinja дозволяє передавати параметри з views в шаблон. Для цього треба використовувати {{}}
```
{% extends "base.html" %}

{% block content %}
  <h1>{{ title }}</h1>
  <ul>
    {% for item in items %}
      <li>{{ item }}</li>
    {% endfor %}
  </ul>
{% endblock %}
```

а також передати з views.py функції параметри у метод render:
```
def my_view(request):
    title = "My Title"
    items = ["Item 1", "Item 2", "Item 3"]
    context = {'title': title, 'items': items}
    return render(request, 'my_template.html', context=context)
```

- Щоб додати статичні файли, треба визначити STATIC_ROOT - директорія, куди в деплої після команди collectstatic будуть переміщені всі статичні файли, а також STATICFILES_DIRS список, куди треба вписати всі директорії, де поки що лежать статичні файли. Статичні файли - всі шрифти, зображення, html, css файли, що є незмінні.

- Якщо використовуються статичні файли в html коді, то вгорі треба написати {% load static %}
Щоб вказати, що сss, js або інше бралося з static, треба його загрузити як статичний елемент:
```
<script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
```

Постійні частини сторінок (topbar, navbar, footer) логічно виносити не в base.html, а по чатсинам в partials/ як окремі файли і загрузити їх в base.html. Так простіше їх правити. Це за допомогою {% include '.html' %}
```
<body>
    {% include 'partials/_topbar.html' %}
    {% include 'partials/_navbar.html' %}
    {% block content %} {% endblock %}
    {% include 'partials/_footer.html' %}

    <script src="{% static 'js/jquery-3.3.1.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>
    <script src="{% static 'js/lightbox.min.js' %}"></script>
    <script src="{% static 'js/main.js' %}"></script>
</body>
```


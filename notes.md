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
15) Add db connection, created models
16) Make migrations, migrate
17) Create superuser 
18) Add some content with admin area
19) Castomize admin area for own style
20) Pull data from models
21) Display listings in template with jinja
22) Make pagination
23) Make Home/About pages
24) Make single listing page
25) make searching with filtering


### Django tips
#### 0.
- django-admin help - список всіх команд від django
#### 1.
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

#### 8.
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

- В urls.py до кожного роута додається параметр name, який потім можна використовувати в html.
Щоб здійснити перехід з сторінки на іншу, використовується:
```
href={% url 'index' %}
```
, де 'index' - ім'я роута


- В кожному файлі кожного застосунку треба створити моделі.

```
class Realtor(models.Model):    
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(datetime.now())
    def __str__(self) -> str:
        return self.name
```


- Щоб додати до БД моделі, треба:
```
python manage.py makemigration
python manage.py sqlmigrate <app_name> 0001 (file counter in migrations/) - дає sql код
python manage.py migrate
```

- Щоб створити superuser, треба:
```
python manage.py createsuperuser
```

- В admin.py ми можемо кастомізувати моделі адмінки для застосунку, тобто додати моделі в адмінку. (admin.py)
```
from .models import Realtor
admin.site.register(Realtor)
```

#### 19. 
Щоб кастомізувати адмін панель, необхідно перш за все створити шаблони html сторінок в templates директорії, наслідуватися від базового шаблону, що дає django
Для кастомізації стилів треба створити в static/css/admin.css та окремо прописувати стилі.

Щоб кастомізувати вивід інфи застосунку в адмінці, треба створити власний клас AppAdmin з наслідуванням від model.ModelAdmin.
Далі списками треба визначити списки того, що буде відображатися в адмін панелі, а також кастомізувати саму адмін панель.
Щоб змінити стилі адмін панелі, необхідно створити template/admin/base_site.html та розширити base/admin.html
```
{% extends 'admin/base.html' %}
{% load static %}

{% block branding %}
    <h1 id='head'>
        <img src="{% static 'img/logo.png' %}" alt="BT Real Estate"
        height="50" width="80" class="brand_img">Admin Area
    </h1>
{% endblock branding %}

{% block extrastyle %}
    <link rel="stylesheet" href="{% static 'css/admin.css' %}">
{% endblock extrastyle %}
```

```
#header {
    height: 50px;
    background: #10284e;
    color: #fff;
}

#branding h1 {
    color: #fff;
}

.colMS > h1 {
    color: #30caa0;
    font-size: large;
    font-weight: 500;
}
```

#### 20. 
Щоб вставляти дані з БД в фронт, треба змінити відповідну функцію обробки запиту в views.py. Також тут відразу додана пагінація, міняти треба в templates.  
```
def index(request):
    listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    paged_listings = paginator.get_page(page_number)
    context = {
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context=context)
```

Pagination
```
{% if listings.has_other_pages %}
            <ul class="pagination">
                {% if listings.has_previous %}
                    <li class="page-item">
                        <a href="?page={{ listings.previous_page_number }}" class="page-link">&laquo;</a>
                    </li>
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link">&laquo;</a>
                    </li>
                {% endif %}

                {% for i in listings.paginator.page_range %}
                    {% if listings.number == i %}
                        <li class="page-item active">
                            <a class="page-link">{{i}}</a>
                        </li>
                    {% else %}
                        <li class="page-item">
                            <a href="?page={{i}}" class="page-link">{{i}}</a>
                        </li>
                    {% endif %}

                {% endfor %}
                
                {% if listings.has_next %}
                    <li class="page-item">
                        <a href="?page={{ listings.next_page_number }}" class="page-link">&raquo;</a>
                    </li>
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link">&laquo;</a>
                    </li>
                {% endif %}
            </ul>
            {% endif %}
```

#### 21
Треба зробити запит з БД і передати його в функцію render(context=context)
```
listings = Listing.objects.all().order_by('-list_date').filter(is_published=True)
context = {
    "listings": listings
}
render(request, 'listings/listings.html, context=context)
```

#### 22
Pagination in templates
```
{% if listings.has_other_pages %}
            <ul class="pagination">
                {% if listings.has_previous %}
                    <li class="page-item">
                        <a href="?page={{ listings.previous_page_number }}" class="page-link">&laquo;</a>
                    </li>
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link">&laquo;</a>
                    </li>
                {% endif %}

                {% for i in listings.paginator.page_range %}
                    {% if listings.number == i %}
                        <li class="page-item active">
                            <a class="page-link">{{i}}</a>
                        </li>
                    {% else %}
                        <li class="page-item">
                            <a href="?page={{i}}" class="page-link">{{i}}</a>
                        </li>
                    {% endif %}

                {% endfor %}
                
                {% if listings.has_next %}
                    <li class="page-item">
                        <a href="?page={{ listings.next_page_number }}" class="page-link">&raquo;</a>
                    </li>
                {% else %}
                    <li class="page-item disabled">
                        <a class="page-link">&laquo;</a>
                    </li>
                {% endif %}
            </ul>
            {% endif %}
```



Щоб передати фото, треба:
```
{{ realtor.photo.url }}
```

Фільтрування даних з БД
listings = Listing.objects.all()
listings = Listing.objects.all().order_by('-list_date')

listings = Listing.objects.order_by('-list_date').filter(id=5) - дає тільки 5 сутність
listings = Listing.objects.order_by('-list_date').filter(description__icontains=keywords) - опис має в собі те, що є в keywords
listings = Listing.objects.order_by('-list_date').filter(city__iexact=city) - ігноруючи lower/upper case, знаходить по місту
listings = Listing.objects.order_by('-list_date').filter(test_gte=60) - great than equal
products = Product.objects.filter(Q(price__gt=50) | Q(category="Електроніка")) - поєднання двох фільтрів через логічний оператор | 




У кожній формі з POST методом має бути csrf_token
```
<form action="{% url 'register' %}" method="POST">
    {% csrf_token %}
</form>
```
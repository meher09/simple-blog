# Django Blogn Setup

## How to create virual environment

- Open terminal or cmd or gitbash
  . write following code

```bash
pip install pipenv
```

- go to the folder you want to create blog
- open command prompt

```bash
pipenv shell
pepenv install django
django-admin startproject core .
python manage.py startapp blog
```

- go to `settings.py` file , add `blog` in installed app
- go to `blog` folder and create following models

```python
from django.db import models

# Create your models here.
class category(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete = models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='images/')
    index_status = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

```

- run following command

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- login url : `localhost:8000/admin`

## To Show admin panel

you need register models

- import models `from .models import Blog, category`

```python
admin.site.register(Blog)
admin.site.register(category)
```

## December 20, 2024

<h2>Views </h2>

```python
from django.shortcuts import render
def about(request):
    return render(request, 'blog/about.html')
```

- create a folder `templates` in `project` folder
- create a folder `blog (your app name) ` in `templates` folder
- create a file `about.html` in `blog` folder

### Data Passed

- data always passed in dictionary format

```python
def about(request):
    data = {
        'name': 'Rahul',
        'age': 25
    }
    return render(request, 'blog/about.html', data)
```

## How to config templates folder

- go to `settings.py` file
- add following code

```python
'DIRS': [BASE_DIR / 'templates'],
```

### url config

- go to `urls.py` file in `project` folder
- add following code

```python
path('', include('blog.urls'))
from django.urls import path, include
```

- create a file `urls.py` in `blog` folder
- add following code

```python
from django.urls import path
from . import views
urlpatterns = [
    path('about/', views.about, name='about')
]
```

### Database Query

home page view

```python
from .models import Blog
def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context)
```

- create a file `home.html` in `blog` folder
- add following code

```html
{% for blog in blogs %}
<h1>{{ blog.title }}</h1>
<p>{{ blog.content }}</p>
{% endfor %}
```

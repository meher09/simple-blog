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

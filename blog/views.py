from django.shortcuts import render
from .models import Blog, category

# Create your views here.

def home(request):
    categories = category.objects.all()
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories
    }
    return render(request, 'blog/home.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    category = blog.category
    related_blogs = Blog.objects.filter(category = blog.category).exclude(slug = slug)[:3]
    context = { 'blog': blog, 'related_blogs': related_blogs, 'category':category }
    return render(request, 'blog/blog_detail.html', context)


def about(request):
    return render(request, 'blog/about.html')


def category_detail(request, slug):
    cat = category.objects.get(slug=slug)
    blogs = Blog.objects.filter(category=cat)
    context = { 'category': cat, 'blogs':blogs }
    return render(request, 'blog/category_detail.html', context)

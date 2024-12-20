from django.shortcuts import render
from .models import Blog, category

# Create your views here.

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/home.html', context)


def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    context = { 'blog': blog }
    return render(request, 'blog/blog_detail.html', context)


def about(request):
    return render(request, 'blog/about.html')
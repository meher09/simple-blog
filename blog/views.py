from django.shortcuts import render
from .models import Blog, category
from django.db.models import Count
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
    comments = blog.comments.filter(active=True)
    print(comments)
    blog.views += 1
    blog.save()
    # category = blog.category

    top_viewed_blogs = Blog.objects.all().order_by('-views')[:3]
    categories = category.objects.annotate(post_count = Count('posts'))




    related_blogs = Blog.objects.filter(category = blog.category).exclude(slug = slug)[:3]
    previous_blog = Blog.objects.filter(created_at__lt = blog.created_at).order_by('-created_at').first()
    next_blog = Blog.objects.filter(created_at__gt = blog.created_at).order_by('created_at').first()
    context = { 'blog': blog, 'related_blogs': related_blogs,
                'category':category, 'previous_blog':previous_blog, 
                'next_blog':next_blog ,
                'top_viewed_blogs':top_viewed_blogs,
                'categories': categories,
                'comments':comments
                }
    return render(request, 'blog/blog_detail.html', context)


def about(request):
    return render(request, 'blog/about.html')


def category_detail(request, slug):
    cat = category.objects.get(slug=slug)
    blogs = Blog.objects.filter(category=cat)
    context = { 'category': cat, 'blogs':blogs }
    return render(request, 'blog/category_detail.html', context)

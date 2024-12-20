from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about-us/', views.about, name='about'),
    path('<slug:slug>/', views.blog_detail, name='blog-detail'),
]

from django.db import models
from django.utils.text import slugify

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField( null =True, blank=True)
    featured_image = models.ImageField(upload_to='category/')
    meta_title = models.CharField(max_length=200, null =True, blank=True)
    meta_description = models.TextField( null =True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name



class Blog(models.Model):
    STATUS = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=200)
    category = models.ForeignKey(category, on_delete = models.CASCADE, blank=True, null=True, related_name='posts')
    slug = models.SlugField(max_length=200, unique=True, null =True, blank=True)
    content = models.TextField( null =True, blank=True)
    featured_image = models.ImageField(upload_to='images/', null=True, blank=True)
    index_status = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200, null =True, blank=True)
    meta_description = models.TextField( null =True, blank=True)
    views = models.IntegerField(default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)





class Comments(models.Model):
    blog  = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'Comments by {self.name} on {self.blog}'
    
    
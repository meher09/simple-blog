from django.db import models
from django.utils.text import slugify

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
    slug = models.SlugField(max_length=200, unique=True, null =True, blank=True)
    content = models.TextField( null =True, blank=True)
    # featured_image = models.ImageField(upload_to='images/')
    index_status = models.BooleanField(default=True)
    meta_title = models.CharField(max_length=200, null =True, blank=True)
    meta_description = models.TextField( null =True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)






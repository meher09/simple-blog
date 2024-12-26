from django.contrib import admin
from .models import Blog, category, Comments
# Register your models here.

admin.site.register(Blog)
admin.site.register(category)
admin.site.register(Comments)

from django.contrib import admin
from blogpost.models import BlogPost

# Register your models here.


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_at']
    list_filter = ['create_at']
    search_fields = ['title']

admin.site.register(BlogPost, BlogPostAdmin)

from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import BlogPost, HomePageContent



admin.site.register(BlogPost, MarkdownxModelAdmin)
admin.site.register(HomePageContent, MarkdownxModelAdmin)

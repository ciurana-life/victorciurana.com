from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

from martor.models import MartorField



class BlogPost(models.Model):
    title = models.CharField(max_length=200, null=True)
    slug = models.SlugField(null=False, unique=True, editable=False)
    content = MartorField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    meta_description = models.CharField(max_length=300, null=True)

    def __str__(self):
        return f'BlogPost - {self.title[:20]}...'

    def get_absolute_url(self) -> str:
        return reverse('blogpost_detail', kwargs={'slug': self.slug})

    def format_date(self) -> str:
        return f'{self.created_at:%Y %m %d}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class HomePageContent(models.Model):
    content = MartorField(null=True)

    def __str__(self):
        return 'Home page content'

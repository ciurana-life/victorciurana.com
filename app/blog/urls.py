from django.urls import re_path
from django.views.decorators.cache import cache_page

from .views import BlogPostDetailView, BlogPostListView

urlpatterns = [
    re_path(
        r"posts/",
        cache_page(60 * 60 * 24, key_prefix="blog")(BlogPostListView.as_view()),
        name="blogpost_list",
    ),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/$",
        cache_page(60 * 60 * 24, key_prefix="blog")(BlogPostDetailView.as_view()),
        name="blogpost_detail",
    ),
]

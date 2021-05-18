from django.urls import path
from django.views.decorators.cache import cache_page

from .views import BlogPostDetailView, BlogPostListView, HomePageContentView

urlpatterns = [
    path(
        "home_page_content/<int:pk>",
        cache_page(60 * 60 * 24)(HomePageContentView.as_view()),
        name="get_home_page_content",
    ),
    path(
        "blog_post_list/",
        cache_page(60 * 60 * 24)(BlogPostListView.as_view()),
        name="get_blog_post_list",
    ),
    path(
        "blog_post_detail/<slug:slug>",
        cache_page(60 * 60 * 24)(BlogPostDetailView.as_view()),
        name="get_blog_post_detail",
    ),
]

from django.urls import path

from .views import BlogPostDetailView, BlogPostListView, HomePageContentView


urlpatterns = [
    path(
        "home_page_content/<int:pk>",
        HomePageContentView.as_view(),
        name="get_home_page_content",
    ),
    path(
        "blog_post_list/",
        BlogPostListView.as_view(),
        name="get_blog_post_list",
    ),
    path(
        "blog_post_detail/<slug:slug>",
        BlogPostDetailView.as_view(),
        name="get_blog_post_detail",
    ),
]

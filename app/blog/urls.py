from django.urls import re_path

from .views import BlogPostDetailView, BlogPostListView

urlpatterns = [
    re_path(r"posts/", BlogPostListView.as_view(), name="blogpost_list"),
    re_path(
        r"(?P<slug>[-a-zA-Z0-9_]+)/$",
        BlogPostDetailView.as_view(),
        name="blogpost_detail",
    ),
]

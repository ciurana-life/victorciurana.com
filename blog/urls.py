from django.urls import path

from .views import *

urlpatterns = [
    path("posts/", BlogPostListView.as_view(), name="blogpost_list"),
    path("<slug:slug>/", BlogPostDetailView.as_view(), name="blogpost_detail"),
]

from django.urls import path
from django.views.decorators.cache import cache_page
from rest_framework import routers

from .views import HomePageContentView, BlogPostViewSet

urlpatterns = [
    path(
        "home_page_content/<int:pk>",
        cache_page(60 * 60 * 24, key_prefix="blog")(HomePageContentView.as_view()),
        name="get_home_page_content",
    )
]

router = routers.SimpleRouter()
router.register(r"blogposts", BlogPostViewSet, basename="BlogPost")
urlpatterns += router.urls

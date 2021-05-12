import pytest
from rest_framework.test import APIRequestFactory

from app.blog.models import BlogPost


@pytest.fixture
def blog_posts():
    for _ in range(20):
        BlogPost.objects.create(title=f"title_{_}", content="Lorem")


@pytest.fixture
def factory():
    factory = APIRequestFactory()
    return factory

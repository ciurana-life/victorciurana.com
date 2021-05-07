from datetime import datetime

import pytest
from django.test import TestCase

from blog.models import BlogPost


# SetUp
@pytest.fixture()
def blog_post():
    blog_post = BlogPost.objects.create(title="test post", content="some content")
    return blog_post


@pytest.mark.django_db
def test_blog_post_created_ok(blog_post):
    bp = BlogPost.objects.first()
    assert bp.slug == "test-post"
    assert type(bp.created_at) == datetime


@pytest.mark.django_db
def test_get_absolute_url(blog_post):
    absolute_url = blog_post.get_absolute_url()
    assert type(absolute_url) == str
    assert absolute_url == "/blog/test-post/"


@pytest.mark.django_db
def test_aut_slug_from_title():
    bp = BlogPost.objects.create(title="Lorem ipsum")
    assert bp.slug == "lorem-ipsum"


@pytest.mark.django_db
def test_format_date_function():
    bp = BlogPost.objects.create(title="Lorem ipsum")
    assert type(bp.format_date()) == str
    assert len(bp.format_date()) == 10

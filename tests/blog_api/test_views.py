import pytest
from django.core.cache import cache
from django.http import response
from django.urls import reverse
from rest_framework import status

from app.blog.models import HomePageContent
from app.blog.views import BlogPostDetailView
from app.config.settings import REST_FRAMEWORK

""" HOME PAGE CONENT """


@pytest.mark.django_db
def test_home_page_content_always_returns_last_or_empty(client):
    # Assert returns empty string when there is no data
    response = client.get(reverse("get_home_page_content", kwargs={"pk": 1}))
    assert response.data["content"] == ""
    assert response.status_code == status.HTTP_200_OK
    # Assert returns last object created
    HomePageContent.objects.create(content="1")
    HomePageContent.objects.create(content="2")
    cache.clear()
    response = client.get(reverse("get_home_page_content", kwargs={"pk": 1}))
    assert response.data["content"] == "2"
    assert response.status_code == status.HTTP_200_OK


""" BLOG POSTS """


def test_pagination_setting_10():
    assert REST_FRAMEWORK["PAGE_SIZE"] == 10


@pytest.mark.django_db
def test_get_all_blog_posts_and_paginates(client, blog_posts):
    response = client.get("/blog_api/blogposts/?page=2")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_blog_post_detail(client, blog_posts):
    response = client.get("/blog_api/blogposts/46/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_get_blog_post_detail_404(client):
    response = client.get("/blog_api/blogposts/50/")
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_get_blog_post_prevents_post(factory):
    request = factory.post("/blog_api/blogposts/15", {"title": "lorem"})
    response = BlogPostDetailView.as_view()(request)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

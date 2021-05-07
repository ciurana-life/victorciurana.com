import pytest
from django.test import Client, RequestFactory

from blog.models import BlogPost
from blog.views import BlogPostDetailView, BlogPostListView, HomePageView


# SetUp
@pytest.fixture()
def blog_post():
    blog_post = BlogPost.objects.create(title="test post", content="some content")
    return blog_post


""" HOME """


@pytest.mark.django_db
def test_home_page_returns_correct_html():
    request = RequestFactory().get("/")
    response = HomePageView.as_view()(request)
    html = response.rendered_content
    assert html.startswith("<!DOCTYPE html>") == True
    assert "<title>Victor Ciurana</title>" in html
    assert html.endswith("</html>") == True
    assert response.status_code == 200


""" POST LIST """


@pytest.mark.django_db
def test_blog_post_list_view_returns_correct_html():
    request = RequestFactory().get("/blog/posts/")
    response = BlogPostListView.as_view()(request)
    html = response.rendered_content
    assert "<title>Blog Posts</title>" in html


@pytest.mark.django_db
def test_blog_post_list_view_response_with_no_posts():
    response = Client().get("/blog/posts/")
    assert "blog/blogpost_list.html" in (t.name for t in response.templates)
    assert len(response.context_data["object_list"]) == 0
    assert response.status_code == 200


@pytest.mark.django_db
def test_blog_post_list_view_response_with_post(blog_post):
    response = Client().get("/blog/posts/")
    assert len(response.context_data["object_list"]) == 1
    assert blog_post in response.context_data["object_list"]
    assert response.status_code == 200


""" POST DETAIL """


@pytest.mark.django_db
def test_blog_post_detail_view_returns_correct_html(blog_post):
    request = RequestFactory().get(blog_post.get_absolute_url)
    response = BlogPostDetailView.as_view()(request, pk=1)
    html = response.rendered_content
    assert html.startswith("<!DOCTYPE html>") == True
    assert "<title>this is a test</title>" in html
    assert '<div class="article_content">' in html
    assert html.endswith("</html>") == True
    assert response.status_code == 200

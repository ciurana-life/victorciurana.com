import pytest
from django.test import RequestFactory

from app.blog.models import BlogPost
from app.blog.views import BlogPostDetailView, HomePageView


# SetUp
@pytest.fixture()
def blog_post():
    blog_post = BlogPost.objects.create(title="test post", content="some content")
    return blog_post


""" Assert newsletter is inserted in views """


@pytest.mark.django_db
def test_newsletter_inserted_in_correct_views(blog_post):
    # Home
    request = RequestFactory().get("/")
    response = HomePageView.as_view()(request)
    html = response.rendered_content
    assert "<h3>Newsletter</h3>" in html
    # Blog post detail
    request = RequestFactory().get(blog_post.get_absolute_url)
    response = BlogPostDetailView.as_view()(request, pk=blog_post.pk)
    html = response.rendered_content
    assert "<h3>Newsletter</h3>" in html

from django.test import Client, RequestFactory, TestCase

from blog.models import BlogPost
from blog.views import BlogPostDetailView, BlogPostListView, HomePageView


class HomePageTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_page_returns_correct_html(self):
        request = self.factory.get("/")
        response = HomePageView.as_view()(request)
        html = response.rendered_content
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertIn("<title>Victor Ciurana</title>", html)
        self.assertTrue(html.endswith("</html>"))
        self.assertEqual(response.status_code, 200)


class BlogPostListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

    def test_html_response(self):
        request = self.factory.get("/blog/posts/")
        response = BlogPostListView.as_view()(request)
        html = response.rendered_content
        self.assertIn("<title>Blog Posts</title>", html)

    def test_response_with_no_posts(self):
        response = self.client.get("/blog/posts/")
        self.assertTemplateUsed(response, "blog/blogpost_list.html")
        self.assertFalse(response.context_data["object_list"])
        self.assertEqual(response.status_code, 200)

    def test_response_with_post(self):
        bp = BlogPost.objects.create(title="Lorem ipsum")
        response = self.client.get("/blog/posts/")
        self.assertTrue(response.context_data["object_list"])
        self.assertIn(bp, response.context_data["object_list"])
        self.assertEqual(response.status_code, 200)


class BlogPostDetailViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.bp = BlogPost.objects.create(title="this is a test", content="lorem ipsum")

    def test_page_renders_ok(self):
        request = self.factory.get(self.bp.get_absolute_url)
        response = BlogPostDetailView.as_view()(request, pk=1)
        html = response.rendered_content
        self.assertTrue(html.startswith("<!DOCTYPE html>"))
        self.assertIn("<title>this is a test</title>", html)
        self.assertIn('<div class="article_content">', html)
        self.assertTrue(html.endswith("</html>"))
        self.assertEqual(response.status_code, 200)

    def test_date_is_formatted_ok(self):
        pass

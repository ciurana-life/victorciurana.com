from datetime import datetime

from django.test import TestCase

from blog.models import BlogPost


class BlogPostModelTest(TestCase):
    def setUp(self):
        self.bp = BlogPost.objects.create(
            title="test post", slug="test_post", content="some content"
        )

    def test_object_created_ok(self):
        bp = BlogPost.objects.first()
        self.assertEqual(bp.slug, "test_post")
        self.assertIsInstance(bp.created_at, datetime)

    def test_get_absolute_url(self):
        absolute_url = self.bp.get_absolute_url()
        self.assertIsInstance(absolute_url, str)
        self.assertEqual(absolute_url, "/blog/test_post/")

    def test_auto_slug_from_title(self):
        bp = BlogPost.objects.create(
            title="Lorem ipsum",
        )
        self.assertEqual(bp.slug, "lorem-ipsum")

    def test_format_date_function(self):
        bp = BlogPost.objects.create(title="Lorem ipsum")
        self.assertIsInstance(bp.format_date(), str)
        self.assertTrue(len(bp.format_date()), 10)

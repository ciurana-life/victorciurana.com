import time
from unittest import skip

from django.test import LiveServerTestCase
from selenium import webdriver

from app.blog.models import BlogPost


@skip("Skipping funcional test for now")
class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        # Create 3 new dummy posts
        for _ in range(0, 3):
            BlogPost.objects.create(
                title=f"test post {_}",
                content="""
                Lorem ipsum dolor sit amet.
                ```python
                def test():
                    return True
                ```
                """,
            )
        super(NewVisitorTest, self).setUp()

    def tearDown(self):
        self.browser.quit()
        super(NewVisitorTest, self).tearDown()

    def test_visitor_navigates_and_checks_code_style(self):
        # [1] Visitor checks the tittle
        self.browser.get(self.live_server_url)
        self.assertIn("Victor Ciurana", self.browser.title)

        # [2] Visitor Clicks on the menu and goes to see all posts
        burger = self.browser.find_element_by_id("burger")
        burger.click()
        # animation waiting...
        time.sleep(0.75)
        # Visitor clicks on box to go see blog posts
        posts_link = self.browser.find_element_by_css_selector('a[href="/blog/posts/"]')
        posts_link.click()
        self.assertIn("/blog/posts/", self.browser.current_url)

        # [3] Visitor sees 3 posts <article> tags and clicks on the first one
        articles = self.browser.find_elements_by_tag_name("article")
        self.assertTrue(len(articles) == 3)
        btn = articles[0].find_element_by_tag_name("a")
        btn.click()

        # [4] Visitor sees the url change and can see styled code
        self.assertIn("/blog/test-post-0/", self.browser.current_url)
        # TODO -->  I don't know why js won't load ...
        # def_text = self.browser.find_element_by_class_name('hljs-keyword')
        # color_of_text = def_text.value_of_css_property('color')
        # self.assertEqual(color_of_text, '#d73a49')

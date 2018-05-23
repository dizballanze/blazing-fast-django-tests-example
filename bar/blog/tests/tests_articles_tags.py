from django.urls import reverse

from blog.tests.base_test_case import BaseBlogTestCase


class ArticlesTagsTestCase(BaseBlogTestCase):

    def setUp(self):
        super().setUp()
        tags = self._create_tags()
        author = self._create_author('foobar', 'foobar@e.co', 'spam', 'v3rys3cr31')
        self._create_article('Spam', 'foo bar', author, True, tags)

    def test_foo_bar(self):
        self.assertEqual(3, 2+1)

    def test_foo_tag_on_articles_list(self):
        resp = self.client.get(reverse('articles_list'))
        self.assertIn('Foo', str(resp.content))

    def test_bar_tag_on_articles_list(self):
        resp = self.client.get(reverse('articles_list'))
        self.assertIn('Bar', str(resp.content))

    def test_spam_tag_on_articles_list(self):
        resp = self.client.get(reverse('articles_list'))
        self.assertIn('Spam', str(resp.content))

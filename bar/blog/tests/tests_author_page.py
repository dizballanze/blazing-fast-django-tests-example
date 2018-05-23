from django.urls import reverse

from blog.tests.base_test_case import BaseBlogTestCase


class AuthorPageTestCase(BaseBlogTestCase):

    def test_foo_bar(self):
        self.assertTrue(True)

    def test_url_resolving(self):
        self.assertEqual(reverse('author_page', kwargs=dict(username='foo-bar')), '/blog/authors/foo-bar')

    def test_author_name_on_its_page(self):
        author = self.authors[0]
        resp = self.client.get(reverse('author_page', kwargs=dict(username=author.username)))
        self.assertIn(author.username, str(resp.content))

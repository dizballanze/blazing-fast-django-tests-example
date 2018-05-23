from django.urls import reverse

from blog.tests.base_test_case import BaseBlogTestCase


class ArticlesListTestCase(BaseBlogTestCase):

    def test_foo_bar(self):
        self.assertEqual(1+1, 2)

    def test_url_resolving(self):
        self.assertEqual(reverse('articles_list'), '/blog/')


class ArticlesListPaginationTestCase(BaseBlogTestCase):

    @classmethod
    def setUpTestData(cls):
        cls.tags = cls._create_tags()
        for author_num in range(5):
            author = cls._create_author(
                'author-{}'.format(author_num), 'author-{}@e.co'.format(author_num), 'Bio #{}'.format(author_num),
                'v3rys3cr31')
            for article_num in range(10):
                cls._create_article(
                    'Article #{}'.format(author_num*10+article_num), 'foo bar', author, True, cls.tags)

    def test_first_20_articles_are_on_the_page(self):
        resp = self.client.get(reverse('articles_list'))
        for i in range(20):
            self.assertIn('Article #{}'.format(i), str(resp.content))

    def test_pagination_works(self):
        resp_page_1 = self.client.get(reverse('articles_list') + '?page=1')
        self.assertEqual(str(resp_page_1.content).count('<article>'), 20)
        resp_page_2 = self.client.get(reverse('articles_list') + '?page=2')
        self.assertEqual(str(resp_page_2.content).count('<article>'), 20)
        resp_page_3 = self.client.get(reverse('articles_list') + '?page=3')
        self.assertEqual(str(resp_page_3.content).count('<article>'), 10)

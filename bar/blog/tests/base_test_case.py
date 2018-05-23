from django.test import TestCase
from blog.models import Article, Author, Tag


class BaseBlogTestCase(TestCase):

    def setUp(self):
        super().setUp()
        tags = [Tag.objects.create(name='Foo'), Tag.objects.create(name='Bar'), Tag.objects.create(name='Spam')]
        self.authors = []
        for author_num in range(5):
            author = Author.objects.create(
                bio='Bio #{}'.format(author_num), email='author{}@e.co'.format(author_num),
                username='author-{}'.format(author_num))
            author.set_password('v3rys3cr31')
            for article_num in range(10):
                article = Article.objects.create(
                    title='Article #{}'.format(author_num * 10 + article_num), content='foo bar', author=author,
                    comments_on=(article_num % 2 == 0))
                article.tags.add(*tags)
            self.authors.append(author)

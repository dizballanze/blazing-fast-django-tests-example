from django.test import TestCase
from blog.models import Article, Author, Tag


class BaseBlogTestCase(TestCase):

    def setUp(self):
        super().setUp()

    def _create_tags(self):
        return [Tag.objects.create(name='Foo'), Tag.objects.create(name='Bar'), Tag.objects.create(name='Spam')]

    def _create_author(self, username, email, bio, password):
        author = Author.objects.create(bio=bio, email=email, username=username)
        author.set_password(password)
        return author

    def _create_article(self, title, content, author, comments_on, tags):
        article = Article.objects.create(title=title, content=content, author=author, comments_on=comments_on)
        if tags:
            article.tags.add(*tags)
        return article

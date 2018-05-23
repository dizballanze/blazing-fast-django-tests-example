from django.test import TestCase
from blog.models import Article, Author, Tag


class BaseBlogTestCase(TestCase):

    def setUp(self):
        super().setUp()

    @classmethod
    def _create_tags(cls):
        return [Tag.objects.create(name='Foo'), Tag.objects.create(name='Bar'), Tag.objects.create(name='Spam')]

    @classmethod
    def _create_author(cls, username, email, bio, password):
        author = Author.objects.create(bio=bio, email=email, username=username)
        author.set_password(password)
        return author

    @classmethod
    def _create_article(cls, title, content, author, comments_on, tags):
        article = Article.objects.create(title=title, content=content, author=author, comments_on=comments_on)
        if tags:
            article.tags.add(*tags)
        return article

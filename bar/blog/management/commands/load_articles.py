import os
import json

from django.core.management.base import BaseCommand
from django.conf import settings

from blog.models import Author, Article, Tag


class Command(BaseCommand):

    help = 'Load articles from `data/old_articles.json`'

    DATA_FILE_PATH = os.path.join(settings.BASE_DIR, '..', 'data', 'old_articles.json')

    def handle(self, *args, **kwargs):
        with open(self.DATA_FILE_PATH, 'r') as json_file:
            data = json.loads(json_file.read())
        for article in data:
            self._import_article(article)

    def _import_article(self, article_data):
        author = Author.objects.get(username=article_data['author'])
        article = Article(
            title=article_data['title'],
            content=article_data['content'],
            created_at=article_data['created_at'],
            author=author)
        article.save()
        tags = []
        for tag in article_data['tags']:
            tag_instance, _ = Tag.objects.get_or_create(name=tag)
            tags.append(tag_instance)
        article.tags.add(*tags)

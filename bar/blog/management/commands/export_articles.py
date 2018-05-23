import os
import csv

from django.core.management.base import BaseCommand
from django.conf import settings

from blog.models import Article


class Command(BaseCommand):

    help = 'Export articles to csv'

    EXPORT_FILE_PATH = os.path.join(settings.BASE_DIR, '..', 'data', 'articles_export.csv')
    COLUMNS = ['title', 'content', 'created_at', 'author', 'comments_on']

    def handle(self, *args, **kwargs):
        with open(self.EXPORT_FILE_PATH, 'w') as export_file:
            articles_writer = csv.writer(export_file, delimiter=';')
            articles_writer.writerow(self.COLUMNS)
            for article in Article.objects.select_related('author').iterator():
                articles_writer.writerow([getattr(article, column) for column in self.COLUMNS])

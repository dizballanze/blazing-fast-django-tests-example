import os
import json

from django.core.management.base import BaseCommand
from django.conf import settings

from blog.models import Author


class Command(BaseCommand):

    help = 'Load authors from `data/old_authors.json`'

    DATA_FILE_PATH = os.path.join(settings.BASE_DIR, '..', 'data', 'old_authors.json')

    def handle(self, *args, **kwargs):
        with open(self.DATA_FILE_PATH, 'r') as json_file:
            data = json.loads(json_file.read())
        author_instances = []
        for author in data:
            author_instances.append(self._import_author(author))
        Author.objects.bulk_create(author_instances)

    def _import_author(self, author_data):
        author = Author(
            username=author_data['username'],
            email=author_data['email'],
            bio=author_data['bio'])
        return author

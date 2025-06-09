from django.core.management.base import BaseCommand
from django.core.management import call_command
from blog.models import Blog

class Command(BaseCommand):
    help = 'Delete all data and load test data from fixture'

    def handle(self, *args, **kwargs):
        # Удаляем существующие записи
        Blog.objects.all().delete()

        # Загружаем данные моделей из фикстуры
        call_command('loaddata', 'blog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Successfully loaded data from fixture'))

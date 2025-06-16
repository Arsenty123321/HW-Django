from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission

import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        group_name = 'Модератор продуктов'

        # Создаем группу
        moderator_group, created = Group.objects.get_or_create(name=group_name)

        # Получаем нужные разрешения
        can_unpublish_permission = Permission.objects.get(codename='can_unpublish_product')
        delete_permission = Permission.objects.get(codename='delete_product')

        # Добавляем разрешения в группу
        moderator_group.permissions.add(can_unpublish_permission, delete_permission)


        if created:
            self.stdout.write(self.style.SUCCESS(f'Группа "{group_name}" была успешно создана.'))
        else:
            self.stdout.write(self.style.WARNING(f'Группа "{group_name}" уже существует.'))

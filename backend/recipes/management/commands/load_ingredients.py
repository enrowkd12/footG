import json
import os

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Загрузка ингредиентов из JSON'

    def handle(self, *args, **kwargs):
        path = os.path.join(
            os.path.dirname(os.path.abspath('manage.py')),
            'data',
            'ingredients.json'
        )
        self.stdout.write(f'Путь к файлу: {path}')
        with open(path, encoding='utf-8') as f:
            data = json.load(f)
        objs = [
            Ingredient(
                name=item['name'],
                measurement_unit=item['measurement_unit']
            )
            for item in data
        ]
        Ingredient.objects.bulk_create(objs, ignore_conflicts=True)
        self.stdout.write(
            self.style.SUCCESS(f'Загружено {len(objs)} ингредиентов')
        )

from django.core.management import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    help = "Создание тегов в БД."

    def handle(self, *args, **kwargs):
        data = [
            {"name": "Горячие блюда", "color": "#F70B07", "slug": "hot"},
            {"name": "Салаты", "color": "#F9FC23", "slug": "salads"},
            {"name": "Закуски", "color": "#0FF225", "slug": "snacks"},
            {"name": "Супы", "color": "#D3E88E", "slug": "soups"},
            {"name": "Выпечка", "color": "#FAC13C", "slug": "bakery products"},
            {"name": "Десерты", "color": "#F51128", "slug": "desserts"},
            {"name": "Напитки", "color": "#1CE8DE", "slug": "drinks"},
            {"name": "Детские блюда", "color": "#D01CE8", "slug": "meals"},
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(
            self.style.SUCCESS("Теги загружены в БД!")
        )

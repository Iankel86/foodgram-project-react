from django.core.management import BaseCommand

from recipes.models import Tag


class Command(BaseCommand):
    help = "Создание тегов в БД."

    def handle(self, *args, **kwargs):
        data = [
            {"name": "Завтрак", "color": "#E26C2D", "slug": "breakfast"},
            {"name": "Обед", "color": "#49B64E", "slug": "dinner"},
            {"name": "Полдник", "color": "#CD853F", "slug": "snack"},
            {"name": "Ужин", "color": "#9ACD32", "slug": "lunch"},
            {"name": "Праздник", "color": "#FF6347", "slug": "holiday"},
            {"name": "Спорт", "color": "#8775D2", "slug": "sport"},
        ]
        Tag.objects.bulk_create(Tag(**tag) for tag in data)
        self.stdout.write(
            self.style.SUCCESS("Теги загружены в БД!")
        )

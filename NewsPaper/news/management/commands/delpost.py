from django.core.management.base import BaseCommand, CommandError
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Удаление статей в определенной категории'  # показывает подсказку при вводе "python manage.py delpost --help"
    missing_args_message = 'Не указаны аргументы'  # выводится, если не указаны аргументы
    requires_migrations_checks = True  # напоминать ли о миграциях. Если тру — то будет напоминание о том, что не сделаны все миграции (если такие есть)

    def add_arguments(self, parser):
        parser.add_argument('category', type=str)  # добавляем аргумент категории

    def handle(self, *args, **options):
        category_name = options.get('category')

        if category_name:
            answer = input(f'Вы правда хотите удалить все статьи в категории {category_name}? (y/n): ')

            if answer.lower() == 'y':
                try:
                    category = Category.objects.get(title=category_name)
                    Post.objects.filter(category=category).delete()
                    self.stdout.write(self.style.SUCCESS(f'Все статьи в категории {category_name} удалены'))
                except Category.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Не найдено категории {category_name}'))
            else:
                self.stdout.write(self.style.ERROR('Отменено'))
        else:
            self.stdout.write(self.style.ERROR('Не указана категория'))

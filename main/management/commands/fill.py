from django.core.management import BaseCommand

from main.models import Customer


class Command(BaseCommand):
    def handle(self, *args, **options):
        customer_list = [
            {'email': 'test1@example.com', 'full_name': 'Иванов Иван Иванович', 'comment': 'comment_test1'},
            {'email': 'test2@example.com', 'full_name': 'Петров Петр Петрович', 'comment': 'comment_test2'},
            {'email': 'test3@example.com', 'full_name': 'Максимов Максим Максимович', 'comment': 'comment_test3'},
            {'email': 'test4@example.com', 'full_name': 'Сергеев Сергей Сергеевич', 'comment': 'comment_test4'},
            {'email': 'test5@example.com', 'full_name': 'Михайлов Михаил Михайлович', 'comment': 'comment_test5'}
        ]
        customers_for_create = []
        for customer_item in customer_list:
            customers_for_create.append(
                Customer(**customer_item)
            )
        Customer.objects.bulk_create(customers_for_create)  # пакетное добавление

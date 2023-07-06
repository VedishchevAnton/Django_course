from django.core.mail import send_mail

from Django_course import settings
from main.models import Message


def send_newsletter(message_item: Message):
    # Получаем список email-адресов клиентов, которым нужно отправить рассылку
    customers_emails = message_item.newsletter.customers.values_list('email', flat=True)

    # Отправляем письмо каждому клиенту
    for email in customers_emails:
        send_mail(
            message_item.subject,  # Тема письма
            message_item.body,  # Тело письма
            settings.EMAIL_HOST_USER,  # От кого отправляем письмо
            [email],  # Кому отправляем письмо
            fail_silently=False,
        )

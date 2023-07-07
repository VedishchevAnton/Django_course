from django.core.mail import send_mail

from Django_course import settings
from main.models import Message, Log


def send_newsletter(message_item: Message):
    # Получаем список email-адресов клиентов, которым нужно отправить рассылку
    customers_emails = message_item.newsletter.customers.values_list('email', flat=True)

    # Отправляем письмо каждому клиенту
    for email in customers_emails:
        try:
            send_mail(
                message_item.subject,  # Тема письма
                message_item.body,  # Тело письма
                settings.EMAIL_HOST_USER,  # От кого отправляем письмо
                [email],  # Кому отправляем письмо
                fail_silently=False,
            )
            status = 'success'
            response = 'Email sent successfully'
        except Exception as e:
            status = 'error'
            response = str(e)
        Log.objects.create(message=message_item, status=status, response=response)


# run crontab
# python manage.py crontab add

# show current active jobs of this project:
# python manage.py crontab show

# removing all defined jobs is straight forward:
# python manage.py crontab remove


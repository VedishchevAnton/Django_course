from django.core.mail import send_mail

from Django_course import settings
from main.models import Message, Log, Newsletter


def daily_send():
    for item in Newsletter.objects.filter(frequency='daily'):
        item.status = 'running'
        item.save()
        send_newsletter(item)
        item.status = 'completed'
        item.save()


def weekly_send():
    for item in Newsletter.objects.filter(frequency='weekly'):
        item.status = 'running'
        item.save()
        send_newsletter(item)
        item.status = 'completed'
        item.save()


def monthly_send():
    for item in Newsletter.objects.filter(frequency='monthly'):
        item.status = 'running'
        item.save()
        send_newsletter(item)
        item.status = 'completed'
        item.save()


def send_newsletter(message_item: Newsletter):
    # Получаем список email-адресов клиентов, которым нужно отправить рассылку
    customers_emails = message_item.customers.values_list('email', flat=True)  # noqa(отключить проверку)

    # Отправляем письмо каждому клиенту
    for email in customers_emails:
        message = Message.objects.create(newsletter=message_item)
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
        Log.objects.create(message=message, status=status, response=response)

# run crontab
# python manage.py crontab add

# show current active jobs of this project:
# python manage.py crontab show

# removing all defined jobs is straight forward:
# python manage.py crontab remove

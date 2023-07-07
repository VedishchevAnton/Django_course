from django.urls import reverse_lazy
from django.views import generic
from main.models import Message, Log
from django.core.mail import send_mail

from Django_course import settings


class MessageCreateView(generic.CreateView):
    model = Message
    template_name = 'main/messages/message_form.html'
    fields = ['newsletter', 'subject', 'body']
    success_url = reverse_lazy('main:messages')

    def form_valid(self, form):
        obj = form.save()
        self.send_newsletter(obj)  # вызываем функцию send_newsletter внутри метода form_valid
        return super().form_valid(form)

    def send_newsletter(self, message_item: Message):
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

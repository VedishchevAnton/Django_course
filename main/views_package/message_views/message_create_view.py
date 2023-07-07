from django.urls import reverse_lazy
from django.views import generic

from main.forms import MessageForm
from main.models import Message

from main.services import send_newsletter


class MessageCreateView(generic.CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'main/messages/message_form.html'
    success_url = reverse_lazy('main:messages')

    # def form_valid(self, form):
    #     obj = form.save()
    #     # send_newsletter(obj)  # вызываем функцию send_newsletter внутри метода form_valid
    #     return super().form_valid(form)

# run crontab
# python manage.py crontab add

# show current active jobs of this project:
# python manage.py crontab show

# removing all defined jobs is straight forward:
# python manage.py crontab remove

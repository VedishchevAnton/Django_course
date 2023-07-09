from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from main.models import Message


class MessageListView(LoginRequiredMixin, generic.ListView):
    model = Message
    template_name = 'main/messages/messages_list.html'
    extra_context = {
        'title': 'Список сообщений'
    }

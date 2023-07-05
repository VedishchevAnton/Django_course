from django.views import generic
from main.models import Message


class MessageListView(generic.ListView):
    model = Message
    template_name = 'main/messages/messages_list.html'
    extra_context = {
        'title': 'Список сообщений'
    }

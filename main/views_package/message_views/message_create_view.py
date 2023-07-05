from django.urls import reverse_lazy
from django.views import generic
from main.models import Message


class MessageCreateView(generic.CreateView):
    model = Message
    template_name = 'main/messages/message_form.html'
    fields = ['newsletter', 'subject', 'body']
    success_url = reverse_lazy('message_list')

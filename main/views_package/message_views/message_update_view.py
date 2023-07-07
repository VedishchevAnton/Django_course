from django.urls import reverse_lazy
from django.views import generic

from main.forms import MessageForm
from main.models import Message


class MessageUpdateView(generic.UpdateView):
    model = Message
    form_class = MessageForm
    template_name = 'main/messages/message_detail.html'
    success_url = reverse_lazy('main:messages')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:message_update', kwargs={'pk': pk})

from django.urls import reverse_lazy
from django.views import generic
from main.models import Message
from main.services import send_newsletter


class MessageCreateView(generic.CreateView):
    model = Message
    template_name = 'main/messages/message_form.html'
    fields = ['newsletter', 'subject', 'body']
    success_url = reverse_lazy('main:messages')

    def form_valid(self, form):
        obj = form.save()
        send_newsletter(obj)
        return super().form_valid(form)
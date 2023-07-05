from django.urls import reverse_lazy
from django.views import generic
from main.models import Message


class MessageDeleteView(generic.DeleteView):
    model = Message
    template_name = 'main/messages/message_confirm_delete.html'
    success_url = reverse_lazy('main:messages')

    def test_func(self):
        return self.request.user.is_superuser  # жесткие требования на удаление (только суперюзер может удалить)

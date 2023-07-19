from django.urls import reverse_lazy
from django.views import generic
from main.models import Newsletter


class NewsletterDeleteView(generic.DeleteView):
    model = Newsletter
    template_name = 'main/newsletters/newsletter_confirm_delete.html'
    success_url = reverse_lazy('main:newsletters')

    def test_func(self):
        return self.request.user.is_superuser  # жесткие требования на удаление (только суперюзер может удалить)

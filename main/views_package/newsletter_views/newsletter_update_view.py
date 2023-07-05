from django.urls import reverse_lazy
from django.views import generic

from main.models import Newsletter


class NewsletterUpdateView(generic.UpdateView):
    model = Newsletter
    fields = ['subject', 'send_time', 'frequency', 'status', 'customers']
    template_name = 'main/newsletters/newsletter_detail.html'
    success_url = reverse_lazy('main:newsletters')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:newsletter_update', kwargs={'pk': pk})


from django.urls import reverse_lazy
from django.views import generic
from main.models import Newsletter


class NewsletterCreateView(generic.CreateView):
    model = Newsletter
    template_name = 'main/newsletters/newsletter_form.html'
    fields = ['subject', 'send_time', 'frequency', 'status', 'customers']
    success_url = reverse_lazy('main:newsletters')

from django.db.models import Count
from django.urls import reverse_lazy
from django.views import generic

from main.forms import NewsletterForm
from main.models import Newsletter
from main.services import send_newsletter


class NewsletterCreateView(generic.CreateView):
    model = Newsletter
    form_class = NewsletterForm
    template_name = 'main/newsletters/newsletter_form.html'
    success_url = reverse_lazy('main:newsletters')

    def form_valid(self, form):
        form.instance.status = 'running'
        response = super().form_valid(form)
        send_newsletter(self.object)
        return response

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        message_item = self.object
        message_item.status = 'running'
        message_item.save()
        send_newsletter(message_item)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletters_count'] = Newsletter.objects.count()
        return context

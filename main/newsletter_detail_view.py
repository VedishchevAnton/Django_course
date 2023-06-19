from django.views import generic
from main.models import Newsletter


class NewsletterDetailView(generic.DetailView):
    model = Newsletter
    template_name = 'main/newsletters/newsletter_detail.html'

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['title'] = context_data['object']

        return context_data

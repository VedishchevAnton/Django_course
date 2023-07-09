from django.views import generic
from main.models import Newsletter


class NewsletterDetailView(generic.DetailView):
    model = Newsletter
    template_name = 'main/newsletters/newsletter_detail.html'

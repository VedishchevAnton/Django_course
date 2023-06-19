from django.views import generic
from main.models import Newsletter


class NewsletterListView(generic.ListView):
    model = Newsletter
    template_name = 'main/newsletters/newsletter_list.html'
    extra_context = {
        'title': 'Список рассылок'
    }

from django.views import generic

from main.models import Log


class LogListView(generic.ListView):
    model = Log
    template_name = 'main/logs/logs_list.html'
    extra_context = {
        'title': 'Список логов'
    }
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from main.models import Log


class LogListView(LoginRequiredMixin, generic.ListView):
    model = Log
    template_name = 'main/logs/logs_list.html'
    extra_context = {
        'title': 'Список логов'
    }
from django.views import generic
from main.models import Log
from main.services import get_cached_log_data


class LogDetailView(generic.DetailView):
    model = Log
    template_name = 'main/logs/log_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['log_data'] = get_cached_log_data(self.object)
        return context

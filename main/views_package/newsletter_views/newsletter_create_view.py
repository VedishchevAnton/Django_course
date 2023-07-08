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

    # Чтобы вызвать метод отправки рассылке клиентам после создания новой рассылки, переопределить метод form_valid()
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        message_item = self.object
        send_newsletter(message_item)
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletters_count'] = Newsletter.objects.count()
        return context

    # Вызываем super().form_valid(form) для сохранения объекта рассылки в базе данных, а затем вызываем
    # send_newsletter() для отправки рассылки всем клиентам, если текущее время находится в диапазоне времени начала
    # и времени окончания рассылки.

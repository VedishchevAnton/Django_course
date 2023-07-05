from django.urls import reverse_lazy
from django.views import generic
from main.models import Newsletter


class NewsletterCreateView(generic.CreateView):
    model = Newsletter
    template_name = 'main/newsletters/newsletter_form.html'
    fields = ['subject', 'send_time', 'frequency', 'status', 'customers']
    success_url = reverse_lazy('main:newsletters')


    # Чтобы вызвать метод отправки рассылке клиентам после создания новой рассылки, переопределить метод form_valid()
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     self.object.send_newsletter()
    #     return response

    # Вызываем super().form_valid(form) для сохранения объекта рассылки в базе данных, а затем вызываем
    # send_newsletter() для отправки рассылки всем клиентам, если текущее время находится в диапазоне времени начала
    # и времени окончания рассылки.

from django.urls import reverse_lazy
from django.views import generic

from main.models import Customer


class CustomerUpdateView(generic.UpdateView):
    model = Customer
    fields = ['email', 'full_name', 'comment']
    template_name = 'main/customers/customer_detail.html'
    success_url = reverse_lazy('main:customers')

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('main:customer_update', kwargs={'pk': pk})

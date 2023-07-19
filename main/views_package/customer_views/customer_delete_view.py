from django.urls import reverse_lazy
from django.views import generic
from main.models import Customer


class CustomerDeleteView(generic.DeleteView):
    model = Customer
    template_name = 'main/customers/customer_confirm_delete.html'
    success_url = reverse_lazy('main:customers')

    def test_func(self):
        return self.request.user.is_superuser  # жесткие требования на удаление (только суперюзер может удалить)
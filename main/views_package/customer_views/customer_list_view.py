from django.views import generic
from main.models import Customer


class CustomerListView(generic.ListView):
    model = Customer
    template_name = 'main/customers/customers_list.html'
    extra_context = {
        'title': 'Список клиентов'
    }

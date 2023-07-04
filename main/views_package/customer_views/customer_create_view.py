from django.urls import reverse_lazy
from django.views import generic
from main.models import Customer


class CustomerCreateView(generic.CreateView):
    model = Customer
    fields = ['email', 'full_name', 'comment']
    template_name = 'main/customers/customer_form.html'
    success_url = reverse_lazy('main:customers')

from django.urls import reverse_lazy
from django.views import generic

from main.forms import CustomerForm
from main.models import Customer


class CustomerCreateView(generic.CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'main/customers/customer_form.html'
    success_url = reverse_lazy('main:customers')

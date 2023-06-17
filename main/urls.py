# URL-адрес (Uniform Resource Locator) Единый указатель ресурсов в интернете
from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, customers

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('customers/', customers, name='customers')
]

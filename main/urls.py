# URL-адрес (Uniform Resource Locator) Единый указатель ресурсов в интернете
from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, customers, newsletters, messages, logs

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('customers/', customers, name='customers'),
    path('newsletters/', newsletters, name='newsletters'),
    path('messages/', messages, name='messages'),
    path('logs/', logs, name='logs'),
]

# URL-адрес (Uniform Resource Locator) Единый указатель ресурсов в интернете
from django.urls import path

from main.apps import MainConfig
from main.newsletter_list_view import NewsletterListView
from main.newsletter_detail_view import NewsletterDetailView
from main.newsletter_create_view import NewsletterCreateView
from main.views import index, contact, customers, messages, logs

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('customers/', customers, name='customers'),
    path('create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletters/', NewsletterListView.as_view(), name='newsletters'),
    path('newsletter/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_item'),
    path('messages/', messages, name='messages'),
    path('logs/', logs, name='logs'),
]

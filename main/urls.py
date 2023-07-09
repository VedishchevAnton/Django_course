# URL-адрес (Uniform Resource Locator) Единый указатель ресурсов в интернете
from django.urls import path
from django.views.decorators.cache import cache_page

from main.apps import MainConfig
from main.views_package.customer_views.customer_create_view import CustomerCreateView
from main.views_package.customer_views.customer_delete_view import CustomerDeleteView
from main.views_package.customer_views.customer_list_view import CustomerListView
from main.views_package.customer_views.customer_update_view import CustomerUpdateView
from main.views_package.index_view.index_view import IndexView
from main.views_package.log_view.log_detail_view import LogDetailView
from main.views_package.log_view.log_list_view import LogListView
from main.views_package.message_views.message_create_view import MessageCreateView
from main.views_package.message_views.message_delete_view import MessageDeleteView
from main.views_package.message_views.message_list_view import MessageListView
from main.views_package.message_views.message_update_view import MessageUpdateView
from main.views_package.newsletter_views.newsletter_delete_view import NewsletterDeleteView
from main.views_package.newsletter_views.newsletter_detail_view import NewsletterDetailView
from main.views_package.newsletter_views.newsletter_list_view import NewsletterListView
from main.views_package.newsletter_views.newsletter_update_view import NewsletterUpdateView
from main.views_package.newsletter_views.newsletter_create_view import NewsletterCreateView
from main.views import contact

app_name = MainConfig.name

urlpatterns = [
    path('', cache_page(5)(IndexView.as_view()), name='index'),
    path('contact/', contact, name='contact'),
    path('customers/', CustomerListView.as_view(), name='customers'),
    path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('customers/delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('newsletters/', NewsletterListView.as_view(), name='newsletters'),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter_create'),
    path('newsletter/newsletter_details/<int:pk>/', NewsletterDetailView.as_view(), name='newsletter_detail'),
    path('newsletter/update/<int:pk>/', NewsletterUpdateView.as_view(), name='newsletter_update'),
    path('newsletter/delete/<int:pk>/', NewsletterDeleteView.as_view(), name='newsletter_delete'),
    path('messages/', MessageListView.as_view(), name='messages'),
    path('messages/create/', MessageCreateView.as_view(), name='message_create'),
    path('messages/update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('messages/delete/<int:pk>/', MessageDeleteView.as_view(), name='message_delete'),
    path('logs/', cache_page(60)(LogListView.as_view()), name='logs'),
    path('log_details/<int:pk>/', LogDetailView.as_view(), name='log_details'),
]

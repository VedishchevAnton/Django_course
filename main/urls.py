# URL-адрес (Uniform Resource Locator) Единый указатель ресурсов в интернете
from django.urls import path

from main.views import index

urlpatterns = [
    path('', index)
]

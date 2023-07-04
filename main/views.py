from django.shortcuts import render

from main.models import Customer, Message, Log


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'main/index.html', context)


# Create your views_package here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contact.html', context)


def customers(request):
    customers_list = Customer.objects.all()
    context = {
        'object_list': customers_list,
        'title': 'Клиенты'
    }

    return render(request, 'main/customers/customers_list.html', context)


def messages(request):
    messages_list = Message.objects.all()
    context = {
        'object_list': messages_list,
        'title': 'Сообщения'
    }

    return render(request, 'main/messages/messages_list.html', context)


def logs(request):
    logs_list = Log.objects.all()
    context = {
        'object_list': logs_list,
        'title': 'Логи'
    }

    return render(request, 'main/logs/logs_list.html', context)

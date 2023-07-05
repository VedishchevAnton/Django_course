from django.shortcuts import render

from main.models import Log


def index(request):
    context = {
        'title': 'Главная',
    }
    return render(request, 'main/index.html', context)


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


def logs(request):
    logs_list = Log.objects.all()
    context = {
        'object_list': logs_list,
        'title': 'Логи'
    }

    return render(request, 'main/logs/logs_list.html', context)

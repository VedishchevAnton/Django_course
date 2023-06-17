from django.shortcuts import render

from main.models import Customer


# Create your views here.
# def index(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         print(f'{name} ({email}): {message}')
#
#     return render(request, 'main/index.html')

def index(request):
    customers_list = Customer.objects.all()
    context = {
        'object_list': customers_list
    }

    return render(request, 'main/index.html', context)

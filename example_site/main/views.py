from django.http import HttpResponse
from django.shortcuts import render


def index_3(request):
    data = {
        'title': 'Главная страница',
        'values': ['123', 'stroka', True],
        'obj': {
            'car': 'BMV',
            'age': 18,
            'hobby': 'football'
        }
    }
    return render(request, 'main/index_3.html', data)


def about_3(request):
    return render(request, 'main/about_3.html')


def contact_3(request):
    return render(request, 'main/index_3.html')


def index_2(request):
    return render(request, 'main/index_2.html')


def about_2(request):
    return render(request, 'main/about_2.html')


def contact_2(request):
    return render(request, 'main/index_2.html')


# HttpResponse подходит для вывода не большого количества информации
def index_1(request):
    return HttpResponse('<h1><center>Главная страница</center></h1>')


def about_1(request):
    return HttpResponse('<h1><center>О нас</center></h1>')


def contact_1(request):
    return HttpResponse('<h1><center>Контакты</center></h1>')




from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/index.html')


# HttpResponse подходит для вывода не большого количества информации
def index_2(request):
    return HttpResponse('<h1><center>Главная страница</center></h1>')


def about_2(request):
    return HttpResponse('<h1><center>О нас</center></h1>')


def contact_2(request):
    return HttpResponse('<h1><center>Контакты</center></h1>')




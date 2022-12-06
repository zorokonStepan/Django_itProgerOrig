from django.http import HttpResponse
from django.shortcuts import render


# HttpResponse подходит для вывода не большого количества информации
def index(request):
    return HttpResponse('<h1><center>Главная страница</center></h1>')


def about(request):
    return HttpResponse('<h1><center>О нас</center></h1>')


def contact(request):
    return HttpResponse('<h1><center>Контакты</center></h1>')


def index_2(request):
    return render(request, 'main/index_2.html')

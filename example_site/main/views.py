from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1><center>Главная страница</center></h1>')


def about(request):
    return HttpResponse('<h1><center>О нас</center></h1>')


def contact(request):
    return HttpResponse('<h1><center>Контакты</center></h1>')


from django.shortcuts import render, redirect

from .models import Article
from .forms import ArticleForm


def news_home(request):
    # news = Article.objects.all()
    # news = Article.objects.order_by('title')
    news = Article.objects.order_by('-date')[:5]  # количество записей
    return render(request, 'news/news_home.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)  # получаем все данные, которые ввел пользователь
        if form.is_valid():  # проверка даннных на корректность
            form.save()  # сохранение данных в БД
            return redirect('news_home')  # переадрисация пользователя на определенную страницу
        else:
            error = 'Форма была не верной'
    else:
        form = ArticleForm()

    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'news/create.html', data)

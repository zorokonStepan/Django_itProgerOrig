from django.shortcuts import render, redirect
# DetailView - позволяет создать контроллер для обработки динамических страниц, вывод определенной записи
# ListView - вывод всех записей
from django.views.generic import DetailView

from .models import Article
from .forms import ArticleForm


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'  # название ключа с помощью которого будет передаваться определенная запись внутрь шаблона


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

from django.shortcuts import render, redirect
# DetailView - позволяет создать контроллер для обработки динамических страниц, вывод определенной записи
# ListView - вывод всех записей
# UpdateView - обновление определенной записи
from django.views.generic import DetailView, UpdateView, DeleteView

from .models import Article
from .forms import ArticleForm


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'  # название ключа с помощью которого будет передаваться определенная запись внутрь шаблона


class NewsUpdateView(UpdateView):
    model = Article
    template_name = 'news/create.html'
    # так не красиво:
    # fields = ['title', 'anons', 'full_text', 'date']  # поля которые будут отображаться
    # так красиво(потому что в ArticleForm указаны все виджеты)
    form_class = ArticleForm


class NewsDeleteView(DeleteView):
    model = Article
    template_name = 'news/delete.html'
    success_url = '/news/'  # куда переадресовать пользователя после удаления записи


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

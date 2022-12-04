from django.shortcuts import render, redirect
from .models import Article
from .forms import ApplicationsForm


def news_home(request):
    news = Article.objects.order_by('-date')[:2]
    return render(request, 'news/index.html', {'news': news})


def create(request):
    error = ''
    if request.method == 'POST':
        form = ApplicationsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма не заполнена'

    form = ApplicationsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)

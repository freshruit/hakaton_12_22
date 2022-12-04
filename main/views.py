from django.shortcuts import render
from news.models import Applications


def index(request):
    return render(request, 'main/index.html')


def works(request):
    works = Applications.objects.all()
    return render(request, 'main/works.html', {'works': works})

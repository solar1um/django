from django.shortcuts import render
from news.models import Article


def main_page(request):
    articles = Article.objects.all()

    return render(request, 'news/index.html',
                  context={'posts': articles})

from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_queryset(self):
        return Article.objects.defer('published_at').select_related('author', 'genre').defer('author__phone')

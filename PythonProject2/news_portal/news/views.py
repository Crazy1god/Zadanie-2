from django.shortcuts import render, get_object_or_404
from .models import Article
from django.http import Http404


def censor(text, bad_words):
    if not isinstance(text, str):
        raise TypeError("Фильтр применяется только к строкам.")

    for word in bad_words:
        text = text.replace(word, '*' * len(word))
    return text


def news_list(request):
    articles = Article.objects.all().order_by('-date')
    bad_words = ['редиска']  # список цензурируемых слов

    for article in articles:
        article.title = censor(article.title, bad_words)
        article.content = censor(article.content, bad_words)

    return render(request, 'news/news_list.html', {'articles': articles})


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    bad_words = ['редиска']  # список цензурируемых слов
    article.title = censor(article.title, bad_words)
    article.content = censor(article.content, bad_words)

    return render(request, 'news/article_detail.html', {'article': article})
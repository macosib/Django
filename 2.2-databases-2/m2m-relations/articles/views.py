from django.db.models import Prefetch
from django.shortcuts import render
from articles.models import Article, ArticleScope, Tag


def articles_list(request):
    template = 'articles/news.html'
    object_list = Article.objects.prefetch_related(
        Prefetch('scopes', queryset=ArticleScope.objects.order_by('-is_main', 'tag__name').all()),
        Prefetch('scopes__tag', queryset=Tag.objects.all()))
    context = {
        'object_list': object_list
    }
    return render(request, template, context)

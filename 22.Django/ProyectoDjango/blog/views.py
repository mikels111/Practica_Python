from django.core import paginator
from django.shortcuts import render, resolve_url, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator
# Create your views here.


def list(request):
    articles = Article.objects.all()  # Sacar todos los articulos
    # Cuantos articulos por página van a aparecer
    paginator = Paginator(articles, 2)
    page = request.GET.get('pagina')  # Recoger el número de la página
    page_articles = paginator.get_page(page)

    return render(request, 'articles/list.html', {
        'title': 'Articles',
        'articles': page_articles
    })


def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    # articles = Article.objects.filter(categories=category);
    return render(request, 'categories/category.html', {
        'category': category
        # 'articles':articles
    })


def article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/detail.html', {
        'article': article
    })

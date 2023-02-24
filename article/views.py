from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import Article, ArticleType

from comment.models import Comment

# Create your views here.
def article_list(request):
    articles = Article.objects.filter(is_deleted=False)
    context = {}
    context['articles'] = articles
    context['article_types'] = ArticleType.objects.all()
    return render(request, "article_list.html", context)

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    # 1-article app->n-models
    article_content_type = ContentType.objects.get_for_model(article)
    comments = Comment.objects.filter(content_type=article_content_type, object_id=article.id)

    context = {}
    context['article'] = get_object_or_404(Article, pk=article_id)
    context['comments'] = comments
    #context['user'] = request.user
    return render(request, "article_detail.html", context)
    # Django2.0: return render_to_response("article_detail.html", context)

def articles_with_type(request, article_type_pk):
    context = {}
    article_type = get_object_or_404(ArticleType, pk=article_type_pk)
    context['articles'] = Article.objects.filter(article_type=article_type)
    context['article_type'] = article_type
    return render(request, 'articles_with_type.html', context)

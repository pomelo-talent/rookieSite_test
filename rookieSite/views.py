#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from article.models import Article

'''def index(request):
    return HttpResponse("Hello World")'''

def home(request):
    context = {}
    return render(request, 'home.html', context)    

def search(request):
    search_words = request.GET.get('wd', '').strip()
    
    # condition: search condition
    condition = None

    # if condition contains spaces
    for word in search_words.split(' '):
        if condition is None:
            # Q: execute complex queries such as containing "&", "|", "~""
            condition = Q(title__icontains=word)
        else:
            condition = condition | Q(title__icontains=word)

    
    search_articles = []
    # if condition does not contain spaces
    if condition is not None:
        # icase's i: ignore upper/lower case
        search_articles = Article.objects.filter(condition)

    context = {}
    context['search_word'] = search_words
    context['search_articles_count'] = search_articles.count()
    context['search_articles'] = search_articles
    return render(request, 'search.html', context)

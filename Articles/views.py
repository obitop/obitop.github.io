from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
import json
@login_required
@csrf_exempt
def ArticleCreate(request):
    context = {}
    form = ArticleForm(request.POST or None)
    context['is_created'] = False
    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=True)
            context['is_created'] = True
            print(obj.title)
            print(obj.content)
            context['obj'] = obj
    context['form'] = form
    return render(request , 'articles/create.html' ,context)

def ArticleSearch(request):
    try:
        q = request.GET['search']   
    except:
        q = None
    try :
        article = Article.objects.get(id=q)
    except:
        article =None
    context = {
        'object' : article
    }
    return render (request , 'articles/search.html' , context=context)

def ArticleDetail(request , pk):
    
    quer = Article.objects.get(id=pk)
    return HttpResponse("hi there")
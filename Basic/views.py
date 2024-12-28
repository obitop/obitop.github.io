from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render

from Articles.models import Article

import random
def home(request):
    authenticated = False
    if request.user.is_authenticated:
        authenticated =True
    article = Article.objects.all()
    context = {
        'objs' : article,
       } 
    return render(request , 'home.html' , context=context)

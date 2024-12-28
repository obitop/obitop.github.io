"""
URL configuration for Basic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views as home_views
from Articles import views as article_views
from accounts import views as accounts_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , home_views.home),
    path('articles/' , article_views.ArticleSearch ),
    path('articles/<int:pk>/' , article_views.ArticleDetail , name  =  'detail'),
    path('articles/create/' , article_views.ArticleCreate, name = 'create'),
    path('login/' , accounts_views.login_view)
    ,path('logout/' , accounts_views.logout_view),
    path ('register/' , accounts_views.register)
]

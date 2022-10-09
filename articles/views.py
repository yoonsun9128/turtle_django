
import random
from turtle import title
from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    return render(request, 'index.html')

# 저녁메뉴 렌덤으로 선택
def dinner(request,name):
    menus = [{'name':'족발','price':3000}, 
            {'name':'햄버거','price':4000}, 
            {'name':'피자','price':2000}, 
            {'name':'치킨','price':8000}, 
            {'name':'초밥','price':9000}, 
            {'name':'닭발','price':6000}]
    pick = random.choice(menus)
    # order_by('-pk')이용해서 배열 거꾸로
    articles = Article.objects.order_by('-pk')
    context = {
        'pick':pick,
        'name':name,
        'menus':menus,
        'articles' : articles,
    }
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')

#request로 받은 메소드가 post 일때 create_review함수 작동
def create_review(request):
    content = request.POST.get('content')
    title = request.POST.get('title')
    article = Article(title=title, content=content)
    article.save()
   
    return redirect('/articles/dinner/무언가/')

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article,
    }
    return render(request, 'detail.html', context)

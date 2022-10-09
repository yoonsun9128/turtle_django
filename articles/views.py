from multiprocessing import context
import random
from django.shortcuts import render
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
    articles = Article.objects.all()
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
    print(request.POST)
    content = {
        'content':content,
    }
    return render(request, 'review_result.html', content)
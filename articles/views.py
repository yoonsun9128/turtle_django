import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request,name):
    menus = [{'name':'족발','price':3000}, 
            {'name':'햄버거','price':4000}, 
            {'name':'피자','price':2000}, 
            {'name':'치킨','price':8000}, 
            {'name':'초밥','price':9000}, 
            {'name':'닭발','price':6000}]
    pick = random.choice(menus)
    context = {
        'pick':pick,
        'name':name,
        'menus':menus
    }
    return render(request, 'dinner.html', context)

def review(request):
    return render(request, 'review.html')
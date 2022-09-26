import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def dinner(request,name):
    menus = ['조발', '햄버거' ,'피자','치킨','초밥','닭발']
    pick = random.choice(menus)
    context = {
        'pick':pick,
        'name':name,
    }
    return render(request, 'dinner.html', context)
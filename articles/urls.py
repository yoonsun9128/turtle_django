from django.urls import path
from articles import views

#index 이름 이겹치는 경우가 있으니 해당 앱의 이름을 적어주면 장고에서도 혼란이 오지 않음!
app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/', views.dinner, name='dinner'), #변수를 지정가능함
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/update/', views.update, name='update'),
    
]
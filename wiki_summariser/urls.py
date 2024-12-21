from django.urls import path

from . import views

urlpatterns = [
     path('', views.main, name='main'),
    path('search_results/', views.search_results, name='search_results'),
    path('choose_article/', views.choose_article, name='choose_article'),
    #path('result/', views.result, name='result'),
]

from django.urls import path
from . import views

from django.conf.urls import url,include
from django.contrib import admin
from rest_framework import routers
from .views import MovieViewSet

app_name = 'urlapi'


urlpatterns = [
    path('', views.CatList.as_view()),
    path('<int:id>', views.CatDetail.as_view()),
    path('p', views.index, name = 'index'),
    path('get', views.get_api),
    path('post', views.post_api),

]
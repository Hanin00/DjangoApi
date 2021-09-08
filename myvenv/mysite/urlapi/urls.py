from django.urls import path
from . import views


app_name = 'urlapi'

urlpatterns=[
    path('', views.CatList.as_view()),
    path('<int:id>', views.CatDetail.as_view()),
    path('p/', views.index, name = 'index'),
    path('get', views.get_api),
    path('post', views.post_api)
]
from django.urls import path
from . import views


app_name = 'urlapi'

urlpatterns=[
    path('', views.CatDetail.as_view())
]
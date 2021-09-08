from django.urls import path
from . import views


app_name = 'urlapi'

urlpatterns=[
    path('<int:id>', views.CatDetail.as_view())
]
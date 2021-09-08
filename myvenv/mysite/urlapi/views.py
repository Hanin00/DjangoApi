from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render

from . import models
from . import serializers

def index(request) :
    return render(request, 'urlapi/index.html')

#get API
class CatDetail(APIView):
    def get(self, request,  format=None):
        cat = models.Cat(name = "안녕하세요 고양이입니다.",locate = "농구장 앞", character = "치즈",
                         preferences = "템테이션 파란색")
        serializer = serializers.CatSerializer(cat)
        return Response(serializer.data)


class CatList(APIView) :
    def get(self, request, format = None):
        cat = models.Cat.objects.all()
        serializer = serializers.CatSerializer(questions, many=True)
        return Response(serializer.data)


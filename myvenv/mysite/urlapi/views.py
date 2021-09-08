from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404

from django.shortcuts import render

from . import models
from . import serializers

def index(request) :
    return render(request, 'urlapi/index.html')

#get API
class CatDetail(APIView):
    def get(self, request,id, format=None):
        cat = get_object_or_404(models.Cat, pk=id)
        serializer = serializers.CatSerializer(cat)
        return Response(serializer.data)


class CatList(APIView) :
    def get(self, request, format = None):
        cat = models.Cat.objects.all()
        serializer = serializers.CatSerializer(cat, many=True)
        return Response(serializer.data)


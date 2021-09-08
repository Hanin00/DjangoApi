from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from django.http.response import HttpResponse
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




@api_view(['GET'])
def get_api(request):
    posts = models.Post.objects.all()
    serialized_posts = serializers.PostSerializer(posts, many = True)
    return Response(serialized_posts.data)

@api_view(['POST'])
def post_api(request):
    if request.method == 'GET':
        return HttpResponse(status = 200)
    if request.method == 'POST':
        serializer = serializers.PostSerializer(data = request.data, many = True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class MovieViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def getMovie(self, request, format = None):
        movie = models.Movie.objects.all()
        serializer_class = serializers.MovieSerializer(movie, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def post_api(request):
        if request.method == 'GET':
            return HttpResponse(status=200)
        if request.method == 'POST':
            serializer = serializers.MovieSerializer(data=request.data, many=True)
            if (serializer.is_valid()):
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

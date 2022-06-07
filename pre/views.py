from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from rest_framework.parsers import JSONParser
from .models import Articale
from .serializers import ArticalSrializer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


# @csrf_exempt
# def Article_list(request):
#     if request.method == 'GET':
#         articles = Articale.objects.all()
#         serializer = ArticalSrializer(articles, many=True)
#         return JsonResponse(serializer.data, safe=False)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = ArticalSrializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data,status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# def Article_detail(request ,pk):
#     try:
#         article = Articale.objects.get(pk = pk)
#     except Articale.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = ArticalSrializer(article)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = ArticalSrializer(article, data = data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=204)

from pre.models import Articale
from pre.serializers import ArticalSrializer
from rest_framework import generics


class ArticleList(generics.ListCreateAPIView):
    queryset = Articale.objects.all()
    serializer_class = ArticalSrializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articale.objects.all()
    serializer_class = ArticalSrializer
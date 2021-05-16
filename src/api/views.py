from _testcapi import raise_exception

from django.shortcuts import get_object_or_404

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from src.blog.models import BlogPost
from .serializers import *


class BlogView(APIView):
    def get(self, request):
        context = {}
        blog_post = BlogPost.objects.prefetch_related()
        blog_post_data = BlogPost.objects.select_related('date_published').all()

        serializer = BlogSerializer(blog_post, many=True)
        context['blog_post'] = serializer.data
        return Response(context)

    def post(self, request):
        blog_post = request.data.get('blog_post')

        serializer = BlogSerializer(data=blog_post)
        if serializer.is_valid(raise_exception=True):
            blog_saved = serializer.save()
        return Response({"success": "BLog '{}' created successfully".format(blog_saved.title)})

@api_view(['GET'])
def blogList(request):
    blogs = BlogPost.objects.all()
    serializer = BlogSerializer(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def blogDetail(request, slug):
    blogs = get_object_or_404(BlogPost, slug=slug)
    serializer = BlogSerializer(blogs, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def blogCreate(request):
    serializer = BlogSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view
def blogUpdate(self, request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    serializer = BlogSerializer(instance=blog, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def blogDelete(request, slug):
    blog = get_object_or_404(BlogPost, slug=slug)
    blog.delete()

    return Response('Deleted')
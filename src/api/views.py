from _testcapi import raise_exception

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from src.blog.models import BlogPost
from src.blog.serializers import BlogSerializer


class BlogView(APIView):
    def get(self, request):
        context = {}
        blog_post = BlogPost.objects.all()
        serializer = BlogSerializer(blog_post, many=True)
        context['blog_post'] = serializer.data
        return Response(context)

    def post(self, request):
        blog_post = request.data.get('blog_post')

        serializer = BlogSerializer(data=blog_post)
        if serializer.is_valid(raise_exception=True):
            blog_saved = serializer.save()
        return Response({"success": "BLog '{}' created successfully".format(blog_saved.title)})

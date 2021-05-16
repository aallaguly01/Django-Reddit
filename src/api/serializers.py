from rest_framework import serializers
from src.blog.models import BlogPost

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
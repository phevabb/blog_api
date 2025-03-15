from django.contrib.auth.models import User
from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Post
        fields = '__all__'


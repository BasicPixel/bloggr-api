from rest_framework import fields
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post

class PostSerializer(ModelSerializer):

    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M", required=False)

    class Meta:
        model = Post
        fields = '__all__'

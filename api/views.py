from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer

# Create your views here.
@api_view(['GET'])
def index(request):
    return Response("Welcome to djreact_blog, read the documentation here: ")

@api_view(['GET'])
def posts(request):
    posts = Post.objects.all().order_by('-timestamp')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)

@api_view(['POST'])
def add_post(request):
    serializer = PostSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)

@api_view(['PUT'])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    serializer = PostSerializer(instance=post, data=request.data)
    serializer.update()

    return Response(serializer.data)

@api_view(['DELETE'])
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()

    return Response("Quote successfully deleted.")

@api_view(['GET'])
def error_404(request, exception=None):
    return Response({'status_code': 404, 'error':'The requested resource was not found.'})
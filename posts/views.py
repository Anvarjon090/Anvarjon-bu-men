from rest_framework.views import APIView
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostListSerializer, PostCreateSerializer


class PostListAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response({"posts": PostListSerializer(posts, many=True).data})


class PostDetailAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return Response({"post": PostListSerializer(post).data})
    

class PostCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer_data = PostCreateSerializer(data=data)
        serializer_data.is_valid(
            raise_exception=True
        )
        post = Post.objects.create(
            **serializer_data.validated_data,
            owner=request.user
            )
        return Response(
            {
                "post": PostListSerializer(post).data
            }
        )
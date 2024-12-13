from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer

class PostPagination(PageNumberPagination):
    page_size = 10

class PostListView(APIView):
    def get(self, request):
        posts = Post.objects.all().order_by('-timestamp')
        paginator = PostPagination()
        paginated_posts = paginator.paginate_queryset(posts, request)
        serializer = PostSerializer(paginated_posts, many=True)
        return paginator.get_paginated_response(serializer.data)
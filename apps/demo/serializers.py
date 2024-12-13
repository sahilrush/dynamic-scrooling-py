from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'timestamp', 'user_username']

class PostSerializer(serializers.ModelSerializer):
    user_username = serializers.CharField(source='user.username', read_only=True)
    comments = serializers.SerializerMethodField()
    comment_count = serializers.IntegerField(source='comments.count', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'text', 'timestamp', 'user_username', 'comments', 'comment_count']

    def get_comments(self, obj):
        comments = obj.comments.order_by('-timestamp')[:3]
        return CommentSerializer(comments, many=True).data
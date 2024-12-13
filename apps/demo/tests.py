from django.test import TestCase
from rest_framework.test import APIClient


from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment

class PostCommentTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.post = Post.objects.create(text="Test Post", user=self.user)
        self.comment = Comment.objects.create(text="Test Comment", post=self.post, user=self.user)

    def test_post_creation(self):
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(self.post.text, "Test Post")

    def test_comment_creation(self):
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(self.comment.text, "Test Comment")
        self.assertEqual(self.comment.post, self.post)

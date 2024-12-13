from django.db import models
from django.contrib.auth.models import User
import uuid


class Post(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Returns a preview of the post's text (first 100 characters)
        return self.text[:100] + ("..." if len(self.text) > 100 else "")


class Comment(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        # Returns a preview of the comment's text (first 100 characters)
        return self.text[:100] + ("..." if len(self.text) > 100 else "")

from django.contrib.auth.models import User
from django.db import models
from blog.models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    active_at = models.BooleanField(default=True)

    def __str__(self):
        return f'{getattr(self.user.profile, "full_name", self.user.username)} - {self.post.title}'

from django.db import models

from lolisgram.models.user_model import User
from lolisgram.models.posts_model import Post

class Comment(models.Model):
    """
    Comment model
    """
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date_commented = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.post.user.username}\'s post'


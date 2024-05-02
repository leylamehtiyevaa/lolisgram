from django.db import models
from lolisgram.models.user_model import User
from lolisgram.models.comments_model import Comment


class Post(models.Model):
    """
    Post model
    """
    image = models.ImageField(upload_to='posts/')
    caption = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    # likes = models.ManyToManyField(User, related_name='likes', blank=True)
    # comments = models.ManyToManyField(Comment, related_name='comments', blank=True)

    def __str__(self):
        return f'{self.user.username}\'s post'
from django.db import models
from lolisgram.models.user_model import CustomUser



class Post(models.Model):
    """
    Post model
    """
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts/')
    caption = models.CharField(max_length=100, blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(CustomUser, related_name='likes', blank=True)


    def __str__(self):
        return f'{self.user.username}\'s post'
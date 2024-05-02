from django.contrib import admin

from lolisgram.models.user_model import User
from lolisgram.models.posts_model import Post
from lolisgram.models.comments_model import Comment


# Register your models here.
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)

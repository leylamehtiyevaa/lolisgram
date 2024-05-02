from django.urls import include, path
from rest_framework import routers

from .views import main_view, user_view, post_view, comment_view

routers = routers.DefaultRouter()
routers.register(r'users', user_view.UserViewSet)
routers.register(r'posts', post_view.PostViewSet)
routers.register(r'comments', comment_view.CommentViewSet)

urlpatterns = [
    path('', main_view.index, name='index'),
    ]
from django.urls import include, path

from .views import main_view


urlpatterns = [
    path('', main_view.index, name='index'),
    #path('api/', include('api.urls')),
    ]
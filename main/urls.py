from django.urls import path

from .views import index, get_article

urlpatterns = [
    path('', index),
    path('posts/', get_article),
]

import requests
from bs4 import BeautifulSoup as bs
from django.urls import path

from .models import Article
from .views import index, get_posts

urlpatterns = [
    path('', index),
    path('posts/<str:qr>/', get_posts),
]


def get_data():
    soup = bs(requests.get('https://news.ycombinator.com/').text)
    all_links = soup.find_all('a', class_='storylink')

    try:
        for link in all_links:
            article = Article(title=link.string, url=link.get('href'))
            article.save()
    except:
        pass
#
# get_data()
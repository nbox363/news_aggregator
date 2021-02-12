import requests
from bs4 import BeautifulSoup as bs
from django.db.utils import IntegrityError
from django.urls import path

from .models import Article
from .views import index, get_article

urlpatterns = [
    path('', index),
    path('posts/', get_article),
]


def get_data():
    soup = bs(requests.get('https://news.ycombinator.com/').text)
    all_links = soup.find_all('a', class_='storylink')

    print('ВОТ')
    try:
        for link in all_links:
            article = Article(title=link.string, url=link.get('href'))
            article.save()
    except IntegrityError:
        pass

get_data()
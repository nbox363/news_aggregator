import requests
from bs4 import BeautifulSoup as bs
from django.apps import AppConfig

from .models import Article


class MainConfig(AppConfig):
    name = 'main'



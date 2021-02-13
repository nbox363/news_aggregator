def get_data():
    from requests import get
    from main.models import Article
    from bs4 import BeautifulSoup
    from django.db.utils import IntegrityError

    r = get('https://news.ycombinator.com/')
    soup = BeautifulSoup(r.text, features='html.parser')
    all_links = soup.find_all('a', class_='storylink')

    try:
        for link in all_links:
            article = Article(title=link.string, url=link.get('href'))
            article.save()
    except IntegrityError:
        pass

get_data()